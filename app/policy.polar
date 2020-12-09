allow(user: User, "read", model) if
    created(user, model);

created(user: User, expense: Expense) if
    expense.created_by = user;

created(user: User, project: Project) if
    project.created_by = user;

allow(user: User, "read", expense: Expense) if
    expense.project in user.projects;

allow(_: User, "read", _: User);
