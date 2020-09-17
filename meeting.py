attendees = ["Dakota", "Taylor", "Kara", "Mary"]
attendees.append("Kyle")
attendees.extend(["Natalie", "Kyle"])
optional_attendees = ["Logan", "Riley"]
potential_attendees = attendees + optional_attendees
print("We may need room for", len(potential_attendees), "people.")
# print("There are", len(attendees), "people joining the meeting!")
#print("Here's who is coming:")
#print(potential_attendees)

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_attendees)
print("To: " + to_line)
print("CC: " + cc_line)