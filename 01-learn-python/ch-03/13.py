glorfindel_perms = 0b0001
galadriel_perms = 0b0010
elendil_perms = 0b0001
elrond_perms = 0b1011

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

# DON'T EDIT ABOVE THIS LINE

party_perms = glorfindel_perms | galadriel_perms | elendil_perms | elrond_perms

# DON'T EDIT BELOW THIS LINE

party_can_create_guild = party_perms & can_create_guild == can_create_guild
party_can_review_guild = party_perms & can_review_guild == can_review_guild
party_can_delete_guild = party_perms & can_delete_guild == can_delete_guild
party_can_edit_guild = party_perms & can_edit_guild == can_edit_guild

print(f"party_perms: 0b{party_perms:b}")
print(f"party_can_create_guild: {party_can_create_guild}")
print(f"party_can_review_guild: {party_can_review_guild}")
print(f"party_can_delete_guild: {party_can_delete_guild}")
print(f"party_can_edit_guild: {party_can_edit_guild}")
