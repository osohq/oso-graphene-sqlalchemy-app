allow(user: User, "read", model) if
    created(user, model);

created(user: User, expense: Expense) if
    expense.created_by = user;

created(user: User, project: Project) if
    project.created_by = user;

allow(user: User, "read", expense: Expense) if
    expense.project in user.projects;

allow(_one: User, "read", _two: User);


def scope custom_roles {
    role_allow(role: RepositoryRole, action: String, resource: Repository);
}

# In hook for creating a custom role:
# oso.add_rule_template(f"role_allow(role: {new_role.name}, action: String, resource: {new_role.resource.class()}");