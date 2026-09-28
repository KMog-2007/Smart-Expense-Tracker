from datetime import datetime
from database import db


class Transaction(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    transaction_type = db.Column(
        db.String(20),
        nullable=False
    )

    amount = db.Column(
        db.Float,
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    description = db.Column(
        db.String(200)
    )

    date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return (
            f"<Transaction "
            f"{self.id}: "
            f"{self.transaction_type} - "
            f"{self.amount}>"
        )