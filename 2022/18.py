def part1(ll):
    raise NotImplementedError

def part2(ll):
    raise NotImplementedError

TEST_INPUT = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

TEST_SOL = [64]

FULL_INPUT = """3,6,12
16,15,16
14,4,14
6,2,7
4,8,16
14,5,7
16,9,3
13,14,6
12,14,1
5,18,13
8,7,16
16,5,8
17,16,12
7,9,3
17,4,11
7,18,7
11,14,19
12,15,5
8,12,2
17,13,16
5,4,14
12,17,6
16,11,16
1,11,9
6,8,17
5,16,6
6,9,4
9,1,11
13,18,8
9,4,17
12,13,2
2,9,9
14,17,14
12,18,5
18,6,11
10,9,3
20,9,12
16,18,9
13,5,18
18,13,7
9,5,13
11,5,2
10,1,8
3,11,10
6,19,9
11,3,17
14,16,4
9,2,15
15,5,4
8,15,4
11,16,15
14,11,2
15,4,9
10,19,12
7,17,16
9,4,15
18,13,10
14,9,4
3,6,8
6,15,6
18,14,9
15,18,12
3,10,9
13,5,16
10,16,15
9,11,20
20,10,13
14,16,6
17,16,9
13,11,2
19,8,7
1,8,14
9,12,20
12,12,2
10,17,18
17,10,5
6,8,19
18,9,7
13,11,19
15,7,18
2,11,10
17,11,16
3,8,7
3,13,14
12,3,9
10,8,18
10,13,2
8,3,9
7,9,2
3,7,9
17,12,4
15,15,4
3,6,10
14,14,19
4,8,5
9,18,12
10,18,16
13,19,14
14,15,6
4,13,14
15,10,17
9,8,3
16,7,6
8,2,9
5,8,4
9,2,9
3,9,9
17,10,7
16,18,10
9,9,17
19,10,8
15,4,15
17,15,5
6,18,8
9,4,16
6,19,11
14,6,16
17,9,5
17,6,9
2,8,14
3,8,9
13,19,13
3,14,8
8,17,15
15,16,7
10,19,7
17,4,14
15,16,13
17,14,14
18,13,6
13,17,5
8,14,18
3,10,15
15,17,14
2,6,11
17,10,15
9,19,10
8,9,2
7,3,5
6,12,6
12,13,19
9,13,1
17,16,10
16,11,3
2,13,11
16,15,14
9,8,19
3,11,15
15,6,17
13,14,19
6,4,14
15,7,4
5,9,17
5,8,5
18,10,11
15,18,11
11,9,19
6,15,16
18,11,7
7,17,9
18,10,12
3,12,10
7,5,13
15,10,3
12,14,3
5,9,18
4,14,17
8,17,11
17,8,18
9,18,16
12,19,8
6,7,17
8,3,14
19,12,14
10,16,18
17,16,13
7,5,16
10,19,10
3,13,5
17,12,16
4,14,14
19,10,9
6,8,5
15,14,4
1,11,11
3,16,9
4,8,15
4,5,14
4,11,17
2,11,9
12,6,17
4,16,14
14,4,10
10,20,10
2,9,11
8,2,7
17,14,7
12,9,3
12,18,7
19,12,10
7,8,15
14,3,9
3,11,8
11,11,18
20,10,10
9,3,10
16,18,11
15,3,9
4,7,3
11,9,3
12,19,7
7,6,6
6,13,5
6,4,12
19,10,15
11,3,16
11,7,2
11,2,10
19,16,10
19,14,11
15,6,5
3,4,10
15,9,15
16,14,17
20,11,10
9,8,20
12,19,10
8,7,18
5,13,19
7,7,6
3,17,11
10,2,11
18,9,16
10,17,15
13,6,18
10,19,9
6,8,18
6,17,8
16,15,15
10,2,7
17,11,6
4,13,8
5,11,4
4,15,10
13,13,4
18,6,6
8,17,4
13,5,7
2,12,14
15,5,16
14,19,13
11,2,14
16,5,6
15,3,7
6,11,3
9,2,14
17,17,13
19,11,7
13,7,18
4,7,8
6,4,16
8,11,2
11,9,1
11,3,10
14,7,18
15,5,6
10,8,1
9,5,3
14,5,15
4,11,7
4,16,11
9,3,6
16,2,10
2,13,10
19,11,13
19,10,12
17,16,11
18,7,7
10,6,2
8,16,18
7,14,3
13,17,11
14,14,2
11,15,16
18,12,11
16,18,12
11,20,14
13,12,2
2,13,12
19,13,13
13,16,14
12,4,15
3,15,9
3,13,6
10,11,2
4,12,7
17,14,11
14,4,6
19,9,7
10,3,14
13,5,5
3,7,7
4,10,6
8,7,17
15,11,18
9,3,8
9,17,14
10,15,3
18,11,11
11,16,4
12,11,1
8,20,13
9,5,6
18,14,14
16,17,12
20,12,8
15,18,7
8,14,19
4,10,5
12,17,5
7,1,11
5,15,4
12,2,14
12,15,17
16,3,11
7,11,4
2,11,8
7,11,3
18,7,8
11,10,17
5,14,8
7,19,14
18,9,12
8,15,2
11,8,20
4,6,14
17,13,17
13,10,3
3,14,12
14,17,15
15,19,10
9,20,8
15,4,12
4,9,8
3,11,14
16,13,16
16,6,4
10,3,4
14,9,3
5,7,5
6,10,5
15,15,17
15,6,15
19,14,8
10,8,2
4,6,7
7,3,15
19,8,11
7,8,17
5,11,17
8,19,9
9,11,1
7,9,18
12,12,1
7,1,8
10,19,13
4,9,5
8,18,15
9,19,12
1,8,12
17,14,9
19,15,13
11,3,8
4,7,16
2,12,9
8,19,6
19,14,7
10,7,19
15,4,14
12,13,17
3,8,8
6,3,14
11,2,13
6,5,14
9,4,5
16,8,5
13,6,5
16,16,6
16,8,18
3,6,7
5,12,4
15,8,18
4,16,6
13,3,9
4,5,8
5,16,12
12,1,11
17,13,13
9,18,15
4,6,5
17,16,16
9,7,2
1,12,9
4,15,14
5,6,9
18,12,7
15,4,5
10,10,3
9,7,3
10,5,16
19,8,8
9,5,16
8,17,18
16,11,5
17,9,16
6,18,11
19,11,9
6,12,1
6,7,15
3,8,10
3,8,16
4,14,8
5,5,8
7,18,13
16,9,4
8,8,1
17,13,7
16,6,14
3,16,7
13,17,10
11,13,19
5,9,13
8,4,11
5,16,14
4,6,8
18,6,10
17,9,6
9,3,11
5,3,11
15,3,13
18,14,10
2,11,12
18,13,16
11,17,6
19,13,8
4,12,5
17,8,8
19,12,7
6,8,3
18,14,12
15,3,10
12,4,5
12,20,10
16,11,17
16,13,3
6,11,17
14,4,17
12,6,3
7,2,10
8,13,19
13,19,6
1,10,12
7,7,18
17,4,7
19,13,14
3,13,9
13,18,7
15,9,4
11,2,11
18,16,9
18,10,14
11,4,16
9,7,13
11,14,1
7,18,14
10,3,13
9,13,4
9,11,19
19,10,6
4,16,13
13,14,2
15,8,4
9,14,3
11,10,2
16,6,10
10,2,9
5,16,7
11,12,2
9,17,5
10,4,17
14,13,18
11,19,10
5,12,16
13,16,6
15,12,4
6,16,14
16,4,12
17,7,6
6,17,12
4,13,13
10,17,2
9,3,15
4,15,13
8,18,8
1,9,9
7,8,2
14,12,19
8,15,3
8,5,16
7,19,8
6,15,15
10,12,17
11,5,6
13,16,17
9,18,14
11,18,10
5,17,9
18,14,13
15,16,16
5,12,14
17,8,6
16,5,12
13,7,3
10,15,18
18,13,13
16,14,14
6,12,15
7,5,6
18,9,8
14,16,7
6,6,15
7,12,2
3,10,12
17,5,8
9,14,18
7,4,14
9,11,2
15,14,7
6,3,16
3,11,9
18,7,12
7,14,19
3,9,12
3,5,12
7,3,6
12,16,17
16,5,7
2,10,12
4,10,16
19,11,12
10,4,6
12,2,7
13,19,9
11,18,13
7,6,13
12,16,2
10,14,5
9,11,3
5,9,6
18,8,15
12,8,3
5,10,17
5,17,13
6,5,15
7,13,4
8,6,19
7,17,5
14,6,3
17,17,10
17,13,6
18,13,11
6,19,13
5,7,11
9,19,7
13,15,17
7,5,15
11,17,16
9,15,18
5,16,5
11,18,17
3,12,16
15,19,12
4,11,13
5,5,9
16,14,6
9,5,18
6,2,11
2,6,10
14,12,2
13,17,6
4,12,8
15,14,5
18,14,7
14,5,6
3,7,14
8,6,17
13,18,6
7,8,4
15,7,7
18,14,8
7,3,9
7,6,18
15,4,16
3,7,10
5,5,7
15,3,11
3,16,8
6,7,13
13,2,6
8,3,11
17,6,10
8,10,2
13,14,3
7,14,18
12,3,15
12,10,19
4,15,7
4,4,12
21,12,12
17,11,5
4,17,13
18,9,5
5,10,16
7,16,17
13,16,16
6,18,6
16,9,5
9,4,14
7,13,5
11,11,2
18,8,14
15,4,6
2,14,12
4,14,15
6,14,17
15,18,13
13,8,3
8,9,3
14,3,14
17,14,12
12,2,11
12,10,18
5,17,11
17,8,12
17,17,11
10,4,7
12,11,18
11,19,13
10,18,9
17,17,7
6,11,1
5,12,17
13,3,8
19,9,9
17,5,11
6,11,18
11,8,2
17,6,15
8,9,1
17,10,17
13,16,3
11,6,4
12,3,11
13,10,19
10,9,18
17,16,14
11,10,19
12,3,13
13,17,17
12,15,16
2,13,16
7,2,13
8,18,13
16,13,17
9,8,18
8,3,13
13,5,3
16,10,9
6,4,10
5,10,4
7,13,18
6,13,4
8,13,2
11,12,20
17,7,14
3,12,9
6,13,17
6,5,9
9,4,4
17,15,11
19,10,10
9,10,17
1,11,12
7,15,3
9,1,9
9,15,16
18,17,8
17,16,6
5,12,6
14,7,6
16,17,14
17,10,18
12,13,18
13,8,16
14,17,6
4,6,11
15,6,12
6,10,3
4,10,9
14,3,13
11,19,9
12,10,2
6,8,2
16,3,14
18,13,8
20,12,10
6,4,9
15,4,10
16,8,15
10,12,20
14,14,18
17,15,15
16,14,5
12,5,18
16,6,17
10,18,13
7,6,5
9,12,2
5,6,15
1,10,11
15,13,17
5,15,5
17,17,12
10,8,3
16,16,16
3,12,4
13,6,16
16,12,18
8,6,18
15,17,8
13,12,3
13,8,18
7,8,19
17,14,15
14,10,3
5,4,9
14,4,5
7,3,7
16,7,7
12,2,9
17,13,15
7,16,16
15,5,15
9,17,16
17,5,14
3,9,3
7,5,5
14,3,7
18,12,14
17,10,4
2,8,10
9,20,12
7,5,4
6,9,2
7,2,7
12,18,14
17,5,15
18,14,11
11,8,4
12,18,9
17,8,5
15,18,10
12,9,20
10,5,13
8,18,10
3,12,5
10,17,14
18,11,8
13,15,3
20,14,11
17,11,17
11,18,14
16,5,11
7,19,10
3,13,11
15,12,16
10,2,10
6,18,13
16,3,10
8,3,7
8,11,19
19,14,9
18,13,17
2,12,13
17,13,5
16,6,15
3,10,7
3,7,6
1,9,12
15,18,14
11,15,4
16,7,15
13,14,17
10,2,14
2,6,9
12,5,5
4,13,18
14,13,4
17,13,14
18,15,9
14,9,17
4,5,10
2,8,7
4,5,11
16,15,6
13,6,3
6,17,15
5,9,10
4,15,6
6,16,11
14,3,8
6,10,19
18,12,6
2,14,10
16,14,16
5,4,11
11,3,14
7,18,5
17,7,16
19,13,11
6,9,16
7,8,16
3,14,7
18,10,7
10,15,4
18,14,15
9,3,14
11,17,4
20,13,8
3,11,7
4,6,13
3,14,10
17,8,14
11,18,9
11,6,3
15,8,16
18,13,14
7,19,9
5,14,17
11,18,8
12,12,19
4,7,4
3,11,17
14,15,17
9,6,2
4,6,10
15,10,18
5,3,9
18,8,11
13,4,7
11,18,15
4,16,7
8,12,20
9,5,8
17,7,17
12,16,5
10,3,8
17,6,13
7,15,18
14,3,12
11,13,3
8,18,6
7,18,10
9,18,6
16,8,4
12,16,4
7,15,5
15,2,9
8,15,16
8,17,13
3,7,13
13,12,19
8,3,8
3,7,8
3,8,6
13,11,16
10,18,5
14,5,5
2,10,8
1,10,8
7,10,4
15,5,8
12,7,18
11,4,5
8,10,1
5,9,3
5,7,7
18,15,10
12,19,14
17,5,9
10,5,7
19,10,13
19,11,10
10,11,21
12,1,9
5,13,18
12,19,12
9,16,17
8,16,5
5,13,16
15,11,2
11,4,10
12,2,8
6,4,15
18,10,5
15,8,5
13,18,10
6,5,6
5,13,17
13,11,20
10,14,4
18,9,6
11,6,17
14,18,8
18,12,8
3,12,8
18,9,14
8,19,7
20,14,10
19,6,9
2,14,11
18,9,9
14,4,8
9,5,17
17,7,8
9,13,19
5,16,4
17,4,8
16,7,13
20,11,9
4,17,11
7,15,4
13,3,16
17,8,4
8,2,12
10,3,10
16,7,4
15,6,16
18,10,10
14,11,16
10,12,18
5,4,6
16,8,3
18,7,6
6,4,11
5,3,10
8,19,10
10,10,2
10,20,9
11,17,13
2,11,11
8,19,14
18,15,12
13,2,9
13,17,15
16,17,7
7,14,4
8,7,4
16,16,7
2,10,14
8,6,4
19,13,12
15,16,8
12,6,19
11,2,5
2,11,5
13,6,4
9,16,18
10,20,12
12,18,15
8,5,8
6,4,5
14,14,17
18,7,15
8,3,15
4,15,5
2,10,6
13,2,7
6,7,6
14,3,11
6,8,14
14,8,17
4,14,5
16,5,5
12,9,2
12,8,19
17,13,8
2,7,10
6,6,4
12,15,18
4,11,18
6,12,7
11,14,2
15,3,14
17,17,9
15,2,10
7,6,10
4,4,11
3,14,15
2,12,8
5,17,12
7,3,13
19,14,12
10,13,19
5,6,6
14,17,9
5,4,13
5,15,10
4,13,17
16,17,15
19,13,9
4,12,16
8,7,19
4,5,12
19,7,13
13,3,12
4,5,13
14,14,8
12,19,9
16,10,15
6,5,13
5,3,13
19,9,11
13,9,17
7,7,3
20,8,10
17,7,7
16,16,14
16,5,9
20,7,13
13,8,17
18,7,13
4,10,7
7,5,17
10,16,3
19,17,10
16,10,7
10,18,14
13,12,18
17,15,14
16,17,9
2,15,11
10,12,19
18,11,9
9,12,1
16,6,16
11,1,14
6,5,11
14,8,3
16,16,15
16,7,18
13,3,17
14,4,11
9,20,11
15,10,4
10,2,13
3,6,15
11,8,19
11,14,3
5,2,12
13,5,4
16,18,13
14,13,2
6,12,16
5,16,15
9,9,1
9,15,8
8,16,16
6,6,8
5,5,6
2,14,9
6,19,12
7,16,18
5,7,13
15,9,3
10,16,17
8,6,2
13,4,15
7,4,10
11,17,5
18,17,11
10,7,3
6,18,12
19,7,9
14,5,4
2,9,10
17,10,6
18,12,15
8,5,14
6,15,17
6,14,7
6,3,11
10,11,20
12,3,6
16,17,10
3,13,15
11,5,3
11,17,10
1,10,6
9,10,19
3,9,6
16,16,13
4,9,4
6,14,3
2,10,7
11,7,20
11,2,9
19,8,14
14,9,18
8,17,14
3,12,6
7,11,2
17,14,8
5,18,10
10,3,6
8,8,19
13,18,11
9,13,2
10,4,16
9,15,4
5,6,12
8,17,10
14,10,18
10,18,11
14,16,17
7,2,9
6,16,6
12,10,3
8,5,6
11,11,17
17,8,9
16,10,17
4,5,7
16,15,4
2,10,9
7,9,17
2,8,13
11,7,18
4,7,15
2,8,12
2,10,10
5,9,4
9,14,2
4,4,9
16,3,12
14,6,9
11,17,3
17,10,16
15,5,5
8,7,15
17,12,5
11,13,18
18,15,13
14,17,8
5,6,7
9,15,5
20,9,13
10,17,16
3,10,4
14,18,7
2,8,9
18,6,9
5,15,6
11,9,2
15,6,4
19,8,13
9,16,3
11,7,3
12,18,8
13,3,7
19,13,7
13,13,19
19,16,13
13,13,18
2,8,6
8,10,19
7,5,3
6,3,15
3,10,5
9,2,10
2,15,10
3,5,10
12,15,2
9,19,14
14,19,15
17,7,12
3,16,10
10,14,2
16,17,6
4,7,17
7,9,4
3,15,15
3,11,12
13,19,11
17,16,7
9,17,15
5,4,7
8,4,15
14,19,12
16,4,9
16,6,9
10,18,10
7,11,19
19,5,9
7,17,8
8,18,9
20,10,9
9,6,15
5,7,4
11,5,4
4,6,15
13,7,16
11,7,5
5,11,5
9,9,19
13,17,14
12,6,4
13,9,20
12,4,4
7,10,3
8,4,6
14,9,20
4,8,6
5,15,15
10,14,18
16,9,16
4,8,13
12,18,11
14,2,7
17,15,12
15,4,13
17,15,16
11,3,15
2,15,8
17,15,17
2,5,10
15,6,18
8,20,14
13,19,8
4,7,12
12,15,3
15,11,3
11,2,12
9,16,4
11,4,13
20,9,9
5,13,12
6,3,9
6,11,19
7,17,7
9,7,16
17,6,11
9,6,17
7,8,3
10,4,3
4,10,10
17,11,7
10,5,17
10,17,6
5,6,11
15,17,6
14,3,6
12,13,3
15,13,5
15,14,16
16,10,4
11,19,11
15,12,18
12,0,10
20,13,12
9,5,4
19,6,12
13,18,14
17,7,5
7,10,2
18,9,13
16,16,12
12,8,18
4,13,16
4,15,8
3,12,14
4,11,16
7,2,14
17,8,13
10,4,12
12,11,20
16,9,14
6,3,8
5,5,5
5,10,18
13,13,8
2,8,8
15,16,4
10,17,5
17,4,10
11,4,17
18,10,9
13,3,14
12,9,1
15,5,7
2,12,7
15,12,17
3,15,13
6,14,5
15,12,5
17,7,11
17,15,4
12,4,14
17,4,12
16,17,13
19,12,12
12,8,16
15,13,4
14,7,15
13,4,17
10,2,15
9,12,19
4,10,17
4,12,17
8,5,17
10,4,14
7,3,14
11,2,8
5,14,2
15,4,17
8,5,15
11,19,6
3,11,6
10,5,18
18,11,5
14,9,5
2,11,13
11,13,20
10,2,8
17,5,7
12,9,4
12,4,6
15,8,2
17,13,11
6,12,3
13,9,3
8,15,18
9,19,9
15,14,17
9,19,6
8,19,8
8,18,14
7,13,19
7,16,5
3,8,13
11,12,1
3,8,15
6,5,12
8,5,18
9,2,12
10,20,11
12,6,2
4,11,8
17,7,9
9,17,6
18,12,13
13,11,3
14,5,17
6,16,5
20,8,11
18,16,11
18,9,15
14,12,4
4,8,7
10,16,19
5,6,4
17,8,15
13,15,14
2,7,9
8,16,17
5,16,13
5,17,14
4,7,7
14,17,11
12,12,20
11,18,7
18,6,13
6,8,16
18,11,13
14,10,19
14,14,3
18,12,17
16,11,4
1,9,13
8,9,16
17,12,10
13,3,13
9,9,2
8,3,12
15,17,15
3,9,5
13,19,12
13,10,2
2,11,6
5,7,15
8,2,11
11,13,1
8,17,16
7,10,18
4,15,16
10,18,17
4,5,15
3,4,9
11,15,3
5,18,8
14,2,11
12,19,15
5,13,4
18,8,9
16,17,8
10,9,19
6,12,17
12,3,10
2,9,12
20,9,10
10,9,2
17,18,14
17,10,14
11,3,6
15,2,12
8,14,2
17,6,8
17,17,14
15,17,5
18,4,14
3,9,14
12,3,8
9,19,8
15,10,16
15,12,20
8,3,16
12,4,16
5,6,5
12,10,20
4,12,9
11,10,20
3,12,15
9,16,6
8,8,2
9,18,11
15,3,6
7,15,19
10,3,9
15,11,14
10,18,12
3,16,11
8,11,20
3,7,11
11,14,18
17,14,13
3,9,11
15,17,12
1,11,8
13,12,4
6,15,9
18,5,11
11,1,11
19,14,13
4,8,8
12,5,3
3,5,11
19,13,10
7,4,6
14,18,14
19,14,14
16,7,3
16,12,16
10,17,4
17,10,8
20,12,9
9,2,6
12,9,18
5,16,9
7,7,5
7,6,4
17,10,3
12,5,4
16,13,4
9,16,5
4,16,16
4,16,9
16,10,18
11,12,19
16,9,19
19,9,12
12,1,13
11,11,20
6,7,4
8,13,18
6,11,2
10,11,19
14,5,3
13,16,11
12,8,4
17,18,10
12,7,17
13,9,18
15,17,9
13,15,8
9,14,17
9,3,5
11,18,16
16,17,11
13,4,4
10,1,10
4,13,15
6,7,14
10,12,2
18,11,12
3,9,16
7,18,12
8,6,3
8,11,1
5,3,7
2,16,11
15,4,7
5,13,15
18,16,7
5,14,9
10,6,18
13,16,7
19,15,11
7,10,19
18,12,12
2,7,13
18,8,10
5,7,17
20,10,12
8,17,9
8,17,17
16,7,16
13,17,7
16,13,6
3,15,11
18,16,12
7,4,7
17,9,14
15,13,3
5,5,13
9,20,13
11,15,2
11,6,16
12,16,3
7,9,1
2,16,9
10,4,13
1,12,7
11,3,5
14,2,8
19,7,11
7,11,18
4,16,10
13,8,20
5,14,5
14,19,10
10,18,6
11,12,0
4,16,8
14,18,11
6,15,13
10,13,3
5,3,8
10,8,19
6,17,6
5,18,7
7,4,8
16,4,14
18,12,16
9,6,19
5,5,14
6,6,16
10,4,18
12,12,3
10,7,2
4,15,15
10,15,6
3,14,13
9,14,16
14,2,6
9,17,3
12,3,5
6,8,4
14,16,5
10,1,11
16,4,15
5,10,15
14,8,4
19,9,14
16,13,5
5,17,15
6,17,9
2,12,12
18,9,11
15,16,12
9,18,3
16,5,13
11,11,1
6,4,6
19,12,11
3,10,6
15,12,3
7,12,18
18,4,8
4,11,15
8,2,8
12,17,15
6,9,18
1,12,10
9,12,17
7,12,17
3,10,16
1,14,10
6,4,13
15,8,17
20,9,8
1,10,9
6,14,18
16,15,13
17,8,17
11,8,1
16,15,12
6,12,18
7,12,15
15,13,6
3,7,16
6,6,17
3,14,9
5,9,16
8,13,17
6,3,13
4,5,6
12,14,18
17,16,15
5,5,16
11,16,16
14,7,16
13,18,17
8,12,16
10,17,13
18,13,15
4,14,12
14,16,16
15,7,5
4,15,9
19,10,11
9,2,7
2,15,7
13,10,18
6,17,14
8,2,10
6,10,6
19,7,14
14,4,15
14,2,10
11,16,5
8,18,16
8,9,17
9,10,2
2,14,13
6,3,7
14,18,9
8,16,4
9,18,17
13,6,17
6,5,7
6,11,4
12,6,16
11,13,15
17,9,9
3,10,13
16,13,2
8,6,16
20,13,13
8,12,19
11,18,5
5,16,16
7,13,3
16,18,8
12,17,4
21,10,10
11,8,3
16,9,17
15,14,6
10,6,19
13,17,4
7,5,12
14,5,16
8,11,18
13,18,9
11,10,18
8,14,17
8,11,5
17,9,13
8,20,10
2,11,14
14,10,17
11,8,17
16,12,13
8,7,3
18,14,6
3,12,7
13,16,19
5,18,14
19,12,6
14,15,5
9,18,10
13,13,2
8,0,11
7,2,11
15,18,6
17,5,10
3,10,10
10,3,11
11,1,13
8,19,13
13,8,4
15,5,14
17,6,7
4,14,16
14,14,15
12,7,2
13,18,13
16,7,14
14,2,9
7,17,13
15,15,7
17,5,13
16,12,4
16,5,14
12,19,16
16,15,8
15,16,17
11,16,1
5,8,7
13,14,5
12,20,14
17,17,8
12,4,17
18,17,13
5,17,8
14,19,7
14,7,7
6,4,17
14,10,4
7,16,13
14,18,5
8,4,5
2,13,13
17,13,4
14,10,2
11,16,11
15,9,20
8,12,18
6,16,16
5,10,5
11,6,5
11,3,9
2,7,14
8,13,3
7,20,12
11,3,7
8,16,13
17,3,10
18,8,12
19,6,13
7,17,6
6,17,10
5,8,15
5,5,12
3,17,7
12,5,13
3,15,8
16,9,18
10,5,3
13,14,4
9,5,9
4,7,13
10,1,9
17,15,13
15,10,2
10,6,6
3,16,12
11,12,17
16,12,5
12,8,2
18,11,6
17,15,8
8,2,14
6,17,7
12,11,17
12,4,7
10,17,17
11,19,14
17,5,12
4,17,10
8,2,15
1,13,13
9,7,4
18,11,16
7,17,12
11,15,19
13,13,1
2,12,6
14,15,8
17,12,14
13,5,17
7,14,15
16,11,6
3,7,15
17,18,12
9,14,19
19,12,9
16,14,15
6,16,17
6,9,7
9,4,6
17,6,4
11,16,18
14,17,4
11,12,3
9,14,4
5,5,15
8,8,4
3,8,5
11,15,14
8,4,14
10,1,7
11,20,12
6,18,7
5,11,15
5,6,16
11,6,19
16,12,11
2,15,13
4,9,11
17,16,8
6,6,6
17,9,15
7,15,15
14,11,18
9,19,11
8,10,18
11,3,12
7,4,16
12,1,10
10,5,5
14,17,12
19,7,12
17,6,14
18,17,9
17,11,14
15,9,5
17,6,6
13,7,17
18,11,14
8,17,6
14,5,8
16,10,6
13,8,19
18,10,13
4,5,9
8,15,19
9,18,5
3,13,7
13,5,15
12,12,18
15,9,16
3,9,13
13,2,8
1,7,9
8,6,6
4,17,8
12,3,7
11,14,4
9,15,17
14,4,7
7,17,14
10,14,3
15,18,8
6,17,11
12,6,5
8,8,3
8,18,11
19,12,13
7,15,14
9,4,8
2,12,16
18,12,9
2,9,15
18,6,14
14,13,3
5,4,12
6,14,6
1,9,11
13,13,20
4,4,14
3,9,17
4,9,6
3,5,13
17,12,7
12,2,13
14,16,14
3,15,12
12,15,6
15,14,18
10,14,16
3,9,15
12,14,4
7,19,12
19,7,10
15,8,15
13,19,7
3,9,7
7,14,2
9,20,10
4,16,15
4,18,9
16,14,3
14,7,3
11,19,16
8,5,4
13,2,10
4,14,13
14,13,5
6,13,3
9,3,13
12,14,2
16,10,5
10,12,1
12,19,13
20,10,11
15,8,7
7,12,19
8,19,15
13,14,18
13,15,18
20,12,12
13,4,5
4,10,14
16,5,15
5,14,7
19,6,10
7,8,18
14,17,10
10,19,11
17,17,15
9,7,19
18,15,8
3,17,10
11,17,17
9,3,16
6,18,9
18,12,5
11,5,17
7,6,3
13,17,16
17,6,12
9,17,13
5,17,10
4,13,5
15,11,6
16,6,6
13,4,14
19,7,8
3,14,14
7,2,12
6,13,18
9,6,18
3,13,8
8,18,7
5,11,18
20,8,9
2,9,8
10,9,17
15,15,14
14,6,5
12,13,16
9,17,17
12,14,17
17,7,4
5,11,3
6,2,8
11,10,1
8,3,6
3,4,12
11,12,18
7,5,9
10,16,4
18,6,8
5,8,17
15,9,2
7,18,11
17,10,13
16,10,16
12,7,20
10,3,7
17,11,15
8,10,3
13,9,19
17,7,15
9,4,18
5,4,10
10,10,1
4,10,3
17,11,18
12,20,11
13,3,6
18,10,16
18,7,5
4,17,9
14,7,5
14,17,17
16,14,7
5,15,17
13,4,16
15,13,15
11,20,9
10,4,5
14,15,19
1,7,12
16,15,11
3,13,12
16,9,9
17,4,9
14,18,12
14,7,17
9,15,3
12,9,17
10,20,7
8,14,4
16,18,7
18,8,13
16,11,14
6,13,19
18,13,9
15,12,19
15,7,12
17,12,17
17,5,5
11,4,6
19,9,10
14,1,8
14,2,13
8,17,7
9,7,18
12,18,10
6,6,7
3,17,9
9,2,11
3,10,17
14,8,19
16,4,7
12,18,13
14,15,18
9,18,7
14,19,9
13,10,16
2,9,14
17,17,6
6,15,4
11,2,7
7,14,16
9,5,15
14,6,6
14,13,19
2,10,11
15,6,14
16,6,5
6,14,15
3,15,6
15,15,3
3,8,14
13,2,14
13,18,12
3,13,4
6,6,5
10,4,15
5,15,16
11,5,16
5,9,5
15,3,12
4,4,8
7,14,17
10,16,5
9,13,18
18,14,16
11,15,18
8,18,5
2,12,10
12,19,11
12,1,12
17,15,10
13,4,12
14,12,17
1,8,13
4,10,15
7,7,4
10,7,15
8,9,19
9,8,5
6,3,12
16,14,4
20,13,9
16,12,7
6,15,5
11,14,17
16,4,10
19,11,14
8,4,9
4,7,14
15,10,19
3,4,14
10,15,2
7,4,15
4,12,13
12,3,12
15,5,12
8,9,18
15,15,18
12,13,4
10,19,6
5,15,14
14,17,7
1,14,12
2,11,16
5,7,9
1,8,7
19,9,13
18,11,15
2,10,13
8,17,5
15,14,3
4,7,5
12,16,6
15,11,15
14,3,5
16,5,16
13,19,10
6,18,14
10,7,1
15,17,10
7,5,7
11,19,8
3,16,15
5,8,6
17,11,3
4,16,12
11,6,2
13,13,5
11,8,18
14,4,12
11,21,10
12,14,19
14,3,16
7,17,17
18,8,6
10,18,8
11,9,20
12,2,12
13,5,6
5,12,18
8,16,14
5,4,5
6,16,15
15,5,13
5,9,12
7,16,14
14,3,18
12,17,17
4,14,6
6,14,4
4,13,4
18,8,7
13,20,11
6,4,7
15,2,11
20,15,10
9,2,8
6,17,4
12,14,20
19,6,11
13,15,5
12,20,12
15,15,5
2,5,12
12,6,18
16,16,8
9,6,3
16,7,8
13,16,5
5,16,10
16,12,19
15,16,14
1,9,10
8,16,3
11,16,8
10,15,15
3,6,14
15,6,3
4,11,6
20,12,13
7,6,17
4,9,16
7,7,17
9,15,2
3,8,12
3,8,11
6,16,9
3,4,8
6,6,13
9,4,13
19,8,15
16,14,18
15,13,18
19,10,5
18,5,13
14,12,18
5,15,12
10,5,6
12,3,14
9,7,1
3,10,14
11,4,4
4,10,4
10,10,19
18,11,17
9,18,13
11,16,14
16,16,9
10,19,8
13,11,18
17,6,5
9,1,13
6,5,10
10,8,4
15,16,9
8,14,5
12,15,7
11,14,16
13,16,4
20,11,8
6,17,13
6,5,8
14,8,2
6,16,4
14,4,16
15,8,3
5,13,14
10,2,12
10,14,17
3,5,14
14,11,5
8,1,10
19,16,11
18,15,5
8,2,13
4,4,13
20,8,12
5,17,7
14,3,10
14,11,17
1,12,12
12,11,2
14,6,18
3,15,14
2,13,7
13,4,6
4,11,5
7,13,17
15,15,16
6,12,2
15,7,3
16,3,13
20,12,14
16,16,10
18,8,8
19,12,5
4,4,6
6,4,8
5,18,12
10,6,3
4,10,12
4,13,6
13,13,17
11,20,10
17,14,6
9,3,7
6,6,10
8,13,4
10,12,3
6,13,16
12,17,9
11,13,2
18,7,11
5,15,13
18,9,4
4,4,10
16,16,11
12,9,19
19,15,12
17,14,4
15,18,15
10,11,1
10,13,17
10,17,3
17,12,15
14,17,5
16,15,17
5,12,5
1,11,10
14,18,6
7,3,11
13,20,12
18,16,6
11,4,15
8,1,11
13,4,11
2,7,11
9,19,13
18,8,16
6,15,7
14,9,2
10,7,18
14,20,10
19,11,8
18,10,4
5,14,16
15,14,12
16,4,8
16,4,13
14,7,2
16,7,9
8,18,12
8,4,7
5,7,14
11,4,7
11,1,9
8,6,5
5,6,8
6,7,18
19,16,8
7,2,8
10,1,14
7,16,4
6,9,3
17,14,16
6,5,5
11,18,4
11,16,6
10,20,14
12,15,4
7,3,8
18,15,11
12,10,17
20,7,10
13,12,16
7,17,15
19,13,15
8,14,3
3,7,5
10,6,4
3,14,11
16,2,9
2,9,7
5,10,19
10,13,18
3,14,5
11,11,19
6,10,18
9,20,14
15,18,9
14,15,3
5,14,4
18,10,15
6,5,18
11,9,18
9,9,20
8,12,3
5,7,3
7,4,5
14,15,7
1,8,8
14,12,3
19,14,10
13,15,15
18,10,8
5,6,17
6,7,3
15,10,5
4,17,12
8,11,17
2,6,8
10,3,16
2,6,7
9,11,4
14,14,16
4,6,6
16,5,10
9,16,8
4,13,9
15,16,10
17,8,16
12,19,6
15,9,17
6,5,4
7,4,4
15,19,11
14,18,13
11,3,13
21,11,13
13,1,11
4,5,5
2,14,8
18,13,5
5,11,16
18,13,4
10,3,15
5,14,15
6,3,5
3,6,13
10,5,2
8,16,15
19,15,9
7,17,11
2,11,15
20,13,11
2,12,11
8,16,10
14,16,13
3,9,8
12,5,6
12,5,17
10,0,11
18,16,13
14,8,18
17,11,4
5,4,8
11,17,18
6,5,17
12,7,16
18,17,12
7,13,15
10,1,12
18,11,10
7,18,15
12,5,15
15,5,10
9,12,18
6,7,16
8,19,11
14,16,15
17,12,6
12,7,3
9,5,5
14,15,16
7,15,16
11,19,5
15,2,15
17,15,7
13,12,17
13,8,2
8,16,7
16,8,16
13,13,3
8,1,12
5,16,8
4,14,9
4,6,9
3,11,11
5,3,14
6,6,14
14,8,16
12,11,4
11,19,12
13,17,12
15,16,6
14,14,5
5,3,12
14,19,6
15,13,16
15,16,15
11,1,10
16,7,19
17,3,8
12,3,4
12,16,18
7,5,18
11,1,8
6,19,10
7,19,11
8,12,4
13,17,8
7,7,15
13,4,13
8,15,17
7,13,16
18,7,9
15,6,6
13,2,11
7,11,20
14,14,9
9,20,9
17,8,7
7,12,3
9,8,2
4,6,12
18,16,15
9,3,9
1,12,11
20,9,11
15,15,15
13,11,1
8,15,6
3,7,12
17,13,10
16,15,5
19,8,10
13,18,4
19,10,14
9,3,17
5,14,14
4,19,11
5,9,14
13,3,4
13,4,10
12,5,19
9,10,1
15,7,15
14,16,9
14,16,18
4,7,10
13,18,15
11,4,14
7,1,12
14,5,9
2,13,14
13,7,2
11,20,8
15,11,4
11,18,6
16,15,9
7,6,16
18,15,7
11,18,11
6,8,6
17,3,11
18,5,12
6,12,5
17,12,12
4,13,3
8,8,20
10,2,6
13,15,4
12,18,6
16,12,3
4,11,4
5,8,9
12,3,16
18,7,10
18,16,14
15,7,17
10,18,7
5,7,8
10,17,12
3,11,13
14,13,16
5,7,16
5,7,6
17,9,7
6,10,2
7,4,17
3,12,12
15,5,17
11,10,3
2,14,7
12,16,19
17,7,3
6,18,10
10,5,19
18,5,14
8,5,3
13,2,13
12,17,16
14,5,14
8,17,12
3,17,12
14,5,11
15,11,19
10,17,7
6,16,12
12,5,16
15,13,19
6,12,4
5,17,17
17,10,12
8,5,5
6,10,15
12,2,10
2,13,8
15,19,7
19,11,11
10,8,16
16,4,11
18,18,11
11,3,11
11,19,7
10,17,9
13,2,12
14,11,19
4,13,12
3,12,13
17,9,10
4,12,4
6,3,10
13,7,19
10,20,8
7,18,8
12,17,8
9,10,20
10,1,13
1,12,13
7,19,6
7,12,4
5,6,14
5,6,10
1,13,10
17,11,13
15,2,13
7,11,17
17,7,10
15,13,13
6,9,5
2,8,11
18,16,10
11,0,13
6,2,13
1,10,10
6,16,7
12,4,12
10,7,16
10,5,15
5,13,5
2,15,9
2,6,12
8,7,2
7,6,9
14,19,8
13,4,3
16,18,15
10,5,4
20,14,12
8,1,14
0,12,11
13,7,4
7,4,12
12,11,3
6,2,12
3,15,10
6,4,4
14,12,1
1,10,13
5,5,17
6,9,19
17,9,4
20,11,13
16,7,17
1,7,11
6,16,13
16,8,17
4,9,7
7,18,9
10,16,16
14,5,12
11,7,19
6,16,10
9,18,4
15,12,15
11,5,9
15,6,7
9,17,4
18,9,10
9,15,19
7,7,20
18,6,15
4,3,9
16,15,10
12,17,7
11,6,1
17,19,10
9,17,9
8,8,18
11,17,11
12,2,15
7,10,1
19,9,16
16,6,13
4,15,12
11,5,5
6,17,5
13,17,9
7,7,2
5,15,9
11,16,3
5,19,10
8,10,17
16,13,14
12,7,19
17,4,15
13,15,6
15,9,18
16,14,8
14,19,11
4,11,14
14,15,14
13,16,15
5,5,11
12,17,18
8,15,5
14,14,6
12,20,8
8,11,3
2,5,14
6,10,4
8,5,13
9,16,16
3,9,18"""

FULL_SOL = []