allow(user: User, "read", expense: Expense) if
    expense.created_by = user;

allow(_: User, "read", _: User);
