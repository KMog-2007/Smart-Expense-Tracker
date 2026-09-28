from flask import Flask, render_template, request, redirect, url_for, flash, Response
from database import db, init_db
from models import Transaction
from sqlalchemy import func, extract
from datetime import datetime
import csv
import io


app = Flask(__name__)

app.secret_key = "smart-expense-tracker-secret-key"

init_db(app)


@app.route("/")
def index():

    search = request.args.get(
        "search",
        ""
    ).strip()

    category = request.args.get(
        "category",
        ""
    ).strip()

    transaction_type = request.args.get(
        "transaction_type",
        ""
    ).strip()

    selected_date = request.args.get(
        "date",
        ""
    ).strip()

    month = request.args.get(
        "month",
        ""
    ).strip()

    query = Transaction.query

    if search:
        query = query.filter(
            Transaction.description.ilike(
                f"%{search}%"
            )
        )

    if category:
        query = query.filter(
            Transaction.category == category
        )

    if transaction_type:
        query = query.filter(
            func.lower(
                Transaction.transaction_type
            ) == transaction_type.lower()
        )

    if selected_date:
        query = query.filter(
            func.date(
                Transaction.date
            ) == selected_date
        )

    transactions = query.order_by(
        Transaction.date.desc()
    ).all()

    categories = db.session.query(
        Transaction.category
    ).distinct().order_by(
        Transaction.category
    ).all()

    categories = [
        item[0]
        for item in categories
    ]

    total_income = db.session.query(
        func.coalesce(
            func.sum(Transaction.amount),
            0
        )
    ).filter(
        func.lower(
            Transaction.transaction_type
        ) == "income"
    ).scalar()

    dashboard_expenses = db.session.query(
        func.coalesce(
            func.sum(Transaction.amount),
            0
        )
    ).filter(
        func.lower(
            Transaction.transaction_type
        ) == "expense"
    ).scalar()

    total_transactions = Transaction.query.count()

    balance = total_income - dashboard_expenses

    total_expense_count = Transaction.query.filter(
        func.lower(
            Transaction.transaction_type
        ) == "expense"
    ).count()

    average_expense = db.session.query(
        func.coalesce(
            func.avg(Transaction.amount),
            0
        )
    ).filter(
        func.lower(
            Transaction.transaction_type
        ) == "expense"
    ).scalar()

    category_spending = db.session.query(
        Transaction.category,
        func.sum(
            Transaction.amount
        ).label("total")
    ).filter(
        func.lower(
            Transaction.transaction_type
        ) == "expense"
    ).group_by(
        Transaction.category
    ).order_by(
        func.sum(
            Transaction.amount
        ).desc()
    ).all()

    highest_category = "None"
    highest_category_amount = 0

    if category_spending:
        highest_category = category_spending[0][0]
        highest_category_amount = float(
            category_spending[0][1]
        )

    highest_category_percentage = 0

    if dashboard_expenses > 0:
        highest_category_percentage = (
            highest_category_amount
            / dashboard_expenses
        ) * 100

    spending_insight = "No expense data available yet."

    if dashboard_expenses > 0:

        if highest_category_percentage >= 50:
            spending_insight = (
                f"Your highest spending category is "
                f"{highest_category}. It accounts for "
                f"{highest_category_percentage:.1f}% "
                f"of your total expenses."
            )

        elif highest_category_percentage >= 30:
            spending_insight = (
                f"{highest_category} is currently your "
                f"largest spending category, accounting "
                f"for {highest_category_percentage:.1f}% "
                f"of your expenses."
            )

        else:
            spending_insight = (
                f"Your spending is distributed across "
                f"multiple categories. "
                f"{highest_category} is the largest category "
                f"at {highest_category_percentage:.1f}%."
            )

    total_expenses = 0
    expense_count = 0
    category_summary = []

    if month:
        try:
            year, month_number = map(
                int,
                month.split("-")
            )

            total_expenses = db.session.query(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0
                )
            ).filter(
                func.lower(
                    Transaction.transaction_type
                ) == "expense",
                extract(
                    "year",
                    Transaction.date
                ) == year,
                extract(
                    "month",
                    Transaction.date
                ) == month_number
            ).scalar()

            expense_count = Transaction.query.filter(
                func.lower(
                    Transaction.transaction_type
                ) == "expense",
                extract(
                    "year",
                    Transaction.date
                ) == year,
                extract(
                    "month",
                    Transaction.date
                ) == month_number
            ).count()

            category_summary = db.session.query(
                Transaction.category,
                func.sum(
                    Transaction.amount
                ).label("total")
            ).filter(
                func.lower(
                    Transaction.transaction_type
                ) == "expense",
                extract(
                    "year",
                    Transaction.date
                ) == year,
                extract(
                    "month",
                    Transaction.date
                ) == month_number
            ).group_by(
                Transaction.category
            ).order_by(
                func.sum(
                    Transaction.amount
                ).desc()
            ).all()

        except (ValueError, TypeError):
            month = ""

    chart_data = db.session.query(
        Transaction.category,
        func.sum(
            Transaction.amount
        ).label("total")
    ).filter(
        func.lower(
            Transaction.transaction_type
        ) == "expense"
    ).group_by(
        Transaction.category
    ).order_by(
        func.sum(
            Transaction.amount
        ).desc()
    ).all()

    chart_labels = [
        item[0]
        for item in chart_data
    ]

    chart_values = [
        float(item[1])
        for item in chart_data
    ]

    return render_template(
        "index.html",
        transactions=transactions,
        categories=categories,
        search=search,
        selected_category=category,
        selected_type=transaction_type,
        selected_date=selected_date,
        month=month,
        total_expenses=total_expenses,
        expense_count=expense_count,
        category_summary=category_summary,
        total_income=total_income,
        dashboard_expenses=dashboard_expenses,
        total_transactions=total_transactions,
        balance=balance,
        chart_labels=chart_labels,
        chart_values=chart_values,
        total_expense_count=total_expense_count,
        average_expense=average_expense,
        highest_category=highest_category,
        highest_category_amount=highest_category_amount,
        highest_category_percentage=highest_category_percentage,
        spending_insight=spending_insight
    )


@app.route(
    "/add",
    methods=["POST"]
)
def add_transaction():

    transaction_type = request.form.get(
        "transaction_type",
        ""
    ).strip().lower()

    amount = request.form.get(
        "amount",
        ""
    ).strip()

    category = request.form.get(
        "category",
        ""
    ).strip()

    description = request.form.get(
        "description",
        ""
    ).strip()

    transaction_date = request.form.get(
        "date",
        ""
    ).strip()

    if transaction_type not in [
        "income",
        "expense"
    ]:
        flash(
            "Please select a valid transaction type.",
            "error"
        )
        return redirect(
            url_for("index")
        )

    try:
        amount = float(amount)

        if amount <= 0:
            flash(
                "Amount must be greater than ₹0.",
                "error"
            )
            return redirect(
                url_for("index")
            )

    except (ValueError, TypeError):
        flash(
            "Please enter a valid amount.",
            "error"
        )
        return redirect(
            url_for("index")
        )

    if not category:
        flash(
            "Category cannot be empty.",
            "error"
        )
        return redirect(
            url_for("index")
        )

    if not transaction_date:
        flash(
            "Please select a transaction date.",
            "error"
        )
        return redirect(
            url_for("index")
        )

    try:
        selected_datetime = datetime.strptime(
            transaction_date,
            "%Y-%m-%d"
        )
    except ValueError:
        flash(
            "Please enter a valid date.",
            "error"
        )
        return redirect(
            url_for("index")
        )

    transaction = Transaction(
        transaction_type=transaction_type,
        amount=amount,
        category=category,
        description=description,
        date=selected_datetime
    )

    db.session.add(transaction)
    db.session.commit()

    flash(
        "Transaction added successfully!",
        "success"
    )

    return redirect(
        url_for("index")
    )


@app.route(
    "/edit/<int:id>",
    methods=["GET", "POST"]
)
def edit_transaction(id):

    transaction = Transaction.query.get_or_404(id)

    if request.method == "POST":

        transaction_type = request.form.get(
            "transaction_type",
            ""
        ).strip().lower()

        amount = request.form.get(
            "amount",
            ""
        ).strip()

        category = request.form.get(
            "category",
            ""
        ).strip()

        description = request.form.get(
            "description",
            ""
        ).strip()

        transaction_date = request.form.get(
            "date",
            ""
        ).strip()

        if transaction_type not in [
            "income",
            "expense"
        ]:
            flash(
                "Please select a valid transaction type.",
                "error"
            )
            return redirect(
                url_for(
                    "edit_transaction",
                    id=id
                )
            )

        try:
            amount = float(amount)

            if amount <= 0:
                flash(
                    "Amount must be greater than ₹0.",
                    "error"
                )
                return redirect(
                    url_for(
                        "edit_transaction",
                        id=id
                    )
                )

        except (ValueError, TypeError):
            flash(
                "Please enter a valid amount.",
                "error"
            )
            return redirect(
                url_for(
                    "edit_transaction",
                    id=id
                )
            )

        if not category:
            flash(
                "Category cannot be empty.",
                "error"
            )
            return redirect(
                url_for(
                    "edit_transaction",
                    id=id
                )
            )

        if not transaction_date:
            flash(
                "Please select a transaction date.",
                "error"
            )
            return redirect(
                url_for(
                    "edit_transaction",
                    id=id
                )
            )

        try:
            selected_datetime = datetime.strptime(
                transaction_date,
                "%Y-%m-%d"
            )
        except ValueError:
            flash(
                "Please enter a valid date.",
                "error"
            )
            return redirect(
                url_for(
                    "edit_transaction",
                    id=id
                )
            )

        transaction.transaction_type = transaction_type
        transaction.amount = amount
        transaction.category = category
        transaction.description = description
        transaction.date = selected_datetime

        db.session.commit()

        flash(
            "Transaction updated successfully!",
            "success"
        )

        return redirect(
            url_for("index")
        )

    return render_template(
        "edit.html",
        transaction=transaction
    )


@app.route(
    "/delete/<int:id>"
)
def delete_transaction(id):

    transaction = Transaction.query.get_or_404(id)

    db.session.delete(transaction)
    db.session.commit()

    flash(
        "Transaction deleted successfully!",
        "success"
    )

    return redirect(
        url_for("index")
    )


@app.route("/export")
def export_csv():

    transactions = Transaction.query.order_by(
        Transaction.date.desc()
    ).all()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "ID",
        "Type",
        "Amount",
        "Category",
        "Description",
        "Date"
    ])

    for transaction in transactions:

        writer.writerow([
            transaction.id,
            transaction.transaction_type,
            transaction.amount,
            transaction.category,
            transaction.description or "",
            transaction.date.strftime("%Y-%m-%d")
            if transaction.date
            else ""
        ])

    response = Response(
        output.getvalue(),
        mimetype="text/csv"
    )

    response.headers["Content-Disposition"] = (
        "attachment; filename=expenses.csv"
    )

    return response


if __name__ == "__main__":

    app.run(
        debug=True
    )