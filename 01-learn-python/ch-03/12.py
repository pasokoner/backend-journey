user_permissions = 0b0110

# DON'T EDIT BELOW THIS LINE

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

user_can_create_guild = user_permissions & can_create_guild == can_create_guild
user_can_review_guild = user_permissions & can_review_guild == can_review_guild
user_can_delete_guild = user_permissions & can_delete_guild == can_delete_guild
user_can_edit_guild = user_permissions & can_edit_guild == can_edit_guild

print(f"user_can_create_guild: {user_can_create_guild}")
print(f"user_can_review_guild: {user_can_review_guild}")
print(f"user_can_delete_guild: {user_can_delete_guild}")
print(f"user_can_edit_guild: {user_can_edit_guild}")
