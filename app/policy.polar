def scope custom {
    allow(user: User, "read", expense: Expense);
}

def scope base {
    allow(user, action, resource);
}

allow(user, action, resource) if
    base::allow(user, action, resource);

allow(user, action, resource) if
    custom::allow(user, action, resource);