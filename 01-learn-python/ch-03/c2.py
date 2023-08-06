user_permissions = 0b1010

read_posts_perm = 0b1000
edit_posts_perm = 0b0100
delete_posts_perm = 0b0010
create_posts_perm = 0b0001

# Don't touch above this line

user_read_posts_perm = user_permissions & read_posts_perm
user_edit_posts_perm = user_permissions & edit_posts_perm
user_delete_posts_perm = user_permissions & delete_posts_perm
user_create_posts_perm = user_permissions & create_posts_perm

# Don't touch below this line

can_read_posts = user_read_posts_perm == read_posts_perm
can_edit_posts = user_edit_posts_perm == edit_posts_perm
can_delete_posts = user_delete_posts_perm == delete_posts_perm
can_create_posts = user_create_posts_perm == create_posts_perm

print(f"The user can read posts: {can_read_posts}")
print(f"The user can edit posts: {can_edit_posts}")
print(f"The user can delete posts: {can_delete_posts}")
print(f"The user can create posts: {can_create_posts}")
