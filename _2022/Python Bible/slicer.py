# Ask the user their email address

email = input("What is your email address?: ").strip()


# Slice out their username

user = email[:email.index("@")]

# Slice out their email provider name
# start 1 after the @ symbol
domain = email[email.index("@") + 1 :]

# Format a message telling the user their username and email provider name
output = "Your username is {} and your domain name is {}".format(user, domain)

# Display the output message
print(output)
