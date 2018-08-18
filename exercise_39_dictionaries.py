peoplesInitials = {
"JD":"John Doe",
"AS":"Alex Smith",
"JB":"Joanne Black",
"TR":"Troy Red",
"PO":"Paul Ottiman"
}

print(f"JD stands for {peoplesInitials['JD']}")

print('-' * 10)

for initial, name in peoplesInitials.items():
    print(initial, " ", name)

print('-' * 10)

so = peoplesInitials.get("SO")

if not so:
    print("SO not found")

print('-' * 10)

print('Another get for SO: ', peoplesInitials.get("SO","SO not found"))
