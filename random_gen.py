import random, csv
greet = ['Hi', 'Hello', 'Hey', 'Good Morning', 'Namaskar']

value1 =random.random()
value2 = random.uniform(1,10)
value3= random.randint(1,8)
value4 = random.choice(greet)
print(value3,value4)
colors = ['red','blue', 'green', 'black']
results = random.choices(colors, weights=[10,10,2,1],k=10) # weights =No of chances each item selected per round , K parameter refers
# no of rounds has to be randomly selected
print(results)
random.shuffle(greet)
print(greet)
print(random.sample(greet,3))
deck =list(range(1,53))
hand = random.sample(deck,k=12)
print(hand)
alpha = ('a','b','c','d','e','f','g')
def name_gen(val):
        name = f'{random.choice(val)}{random.choice(val)}{random.choice(val)}{random.choice(val)}John'
        phone =f'{random.randint(9000000000,9999999999)}'
        emaild = f'{name}@fakemail.com'
        return name + ',' + phone + ',' + emaild + '\n'
with open('fakename.csv','w') as f:
    for item in range(10):
        if item == 0:
            f.writelines('name,phone,email\n')
        else:
            obj1 = name_gen(alpha)
            f.writelines(obj1)



with open('fake.csv','r') as fr:
    csv_read  = csv.DictReader(fr) #    we can use delimiter keyword like delimiter='-' or '\t' etc

    for line in csv_read:
        print(line)
# def gen_gen(gobj,n):
#     for i in range(n):
#         yield gobj.next()

# with open('fakename.csv','w') as f:
#     csv_writer = csv.writer(f)
#     for item in range(10):
#         obj1 = str(name_gen(alpha))
#         print(obj1)
#         csv_writer.writerow(obj1)


