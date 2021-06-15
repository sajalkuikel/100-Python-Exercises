a = ["1", 1, "1", 2]

a = list(set(a))

print(a)

# Explanation 1:
# We used a set  function to convert the list to a set which would intermediately produce {'1', 1, 2}
# with no duplicates because set objects cannot contain duplicates.
# Then using list  we converted the set back to a list.
# The drawback here is that the original order of the items is lost.
