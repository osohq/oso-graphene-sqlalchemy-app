allow(user: User, "read", model) if
    created(user, model);

created(user: User, expense: Expense) if
    expense.created_by = user;

allow(_: User, "read", _: User);
