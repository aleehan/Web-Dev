n = int(input())
nums = input().split()
participants = set()

for i in nums:
    participants.add(int(i))

sorted_participants = sorted(participants)

print(sorted_participants[len(sorted_participants) - 2])