{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "423f9ec7-44bf-4224-815d-41e07da902d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "30ca70b9-db45-46cd-ad6d-982889b9a0e5",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7cbd332-c3ec-4a26-b50e-44b720a23cf3",
   "metadata": {},
   "source": [
    "1. How many negative numbers are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "af289ea2-cf1f-471f-996c-59715428a1f5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 4, 10, 12, 23, -2, -1,  0,  0,  0, -6,  3, -7])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "aa3b429f-5d8a-4054-919b-346ed4d7eba4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 3, -7,  0, -1])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "negative_numbers = a[a < 0]\n",
    "\n",
    "a[negative_numbers]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "947fd176-2296-4504-91e4-2db8b9beb75e",
   "metadata": {
    "tags": []
   },
   "source": [
    "4 negative numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "036051dd-8666-4b0d-b515-620860ddbcff",
   "metadata": {},
   "source": [
    "2. How many positive numbers are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "53f1bfc0-da44-478f-99fe-6a0d064cd51c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 4 10 12 23  3]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])\n",
    "\n",
    "positive_numbers = a[a > 0]\n",
    "\n",
    "print(positive_numbers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1af3bbc0-8e7e-46aa-8a6e-096708984d5e",
   "metadata": {},
   "source": [
    "5 positve numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2dee2dec-e70a-427f-b2fe-5e1b311c3dd4",
   "metadata": {},
   "source": [
    "3. How many even positive numbers are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5f04679a-7e28-4907-9f72-cd2e12109078",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 4 10 12]\n"
     ]
    }
   ],
   "source": [
    "positive_even = a[(a > 0) & (a % 2 == 0)]\n",
    "\n",
    "print(positive_even)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b22c379-a062-4be9-95a4-775b87da0e25",
   "metadata": {},
   "source": [
    "3 positive even numbers "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a46a03e2-e1b1-441b-a571-6949bbeee016",
   "metadata": {},
   "source": [
    "4. If you were to add 3 to each data point, how many positive numbers would there be?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "8784ff27-4c2b-49de-8149-93cb865e8fdd",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 7 13 15 26  1  2  3  3  3 -3  6 -4]\n",
      "[ 7 13 15 26  1  2  3  3  3  6]\n"
     ]
    }
   ],
   "source": [
    "plus_3 = a + 3\n",
    "\n",
    "print(plus_3)\n",
    "positive_numbers_plus_3 = plus_3[plus_3 > 0]\n",
    "\n",
    "print(positive_numbers_plus_3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "274067a6-559c-4895-8ecd-99c50e539db0",
   "metadata": {},
   "source": [
    "10 numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a50369b2-deb8-4385-bc55-30f650a66ffd",
   "metadata": {},
   "source": [
    "5. If you squared each number, what would the new mean and standard deviation be?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "d6e542e4-2f5e-4eca-86dd-bfce951e2908",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 16 100 144 529   4   1   0   0   0  36   9  49]\n",
      "Mean: 74.0\n",
      "Standard deviation: 144.0243035046516\n"
     ]
    }
   ],
   "source": [
    "squared_values = a ** 2\n",
    "print(squared_values)\n",
    "\n",
    "mean = np.mean(squared_values)\n",
    "\n",
    "# Standard Deviation\n",
    "std_dev = np.std(squared_values)\n",
    "\n",
    "print(\"Mean:\", mean)\n",
    "print(\"Standard deviation:\", std_dev)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c12235f-4b8e-49e0-af3b-b79b654a2a24",
   "metadata": {},
   "source": [
    "6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "942b4f9d-fb35-4ba5-b428-cd6121f0c413",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Centered Data: [-70. -64. -62. -51. -76. -75. -74. -74. -74. -80. -71. -81.]\n"
     ]
    }
   ],
   "source": [
    "# Centered data\n",
    "ctd_data = a - mean\n",
    "\n",
    "print(\"Centered Data:\", ctd_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42f97faa-550c-4099-a277-5498a64d13ef",
   "metadata": {},
   "source": [
    "7. Calculate the z-score for each data point."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "62cfd226-d356-438f-a8a4-0a0f6de70aeb",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Z-score: [-0.48602908 -0.44436945 -0.4304829  -0.3541069  -0.52768872 -0.52074544\n",
      " -0.51380217 -0.51380217 -0.51380217 -0.55546181 -0.49297235 -0.56240508]\n"
     ]
    }
   ],
   "source": [
    "# Z-score = centered data / standard deviation\n",
    "z_score = ctd_data / std_dev\n",
    "\n",
    "print(\"Z-score:\", z_score)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6fd9bf8-7cf4-467b-aa29-a030f998569a",
   "metadata": {},
   "source": [
    "8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "24ae41f6-0521-4093-a624-02be028bb292",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Setup 1\n",
    "a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c5029ab-589e-43dd-ab1c-7aa122818882",
   "metadata": {},
   "source": [
    "Use python's built in functionality/operators to determine the following:\n",
    "# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "dd6c7125-98e2-4ba3-9857-219daa1e6afc",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n"
     ]
    }
   ],
   "source": [
    "sum_of_a = sum(a1)\n",
    "\n",
    "print(sum_of_a)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62d6c4ec-5d5c-44b8-bd02-641ef79e80c6",
   "metadata": {},
   "source": [
    "# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "1b9f287c-6911-452f-b040-50e96bc93ba4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "min_of_a = min(a1)\n",
    "\n",
    "print(min_of_a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2248f0c8-713f-4d1a-9176-20bd67f315e4",
   "metadata": {},
   "source": [
    "# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "d316d3b2-187d-406c-a99a-6083a06332aa",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "max_of_a = max(a1)\n",
    "\n",
    "print(max_of_a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dbdd835d-59b1-4ac3-ae2f-555a36eb1936",
   "metadata": {},
   "source": [
    "# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "6ce27fe1-c79f-4a79-94cb-f98b6adcd2cb",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.5\n"
     ]
    }
   ],
   "source": [
    "mean_of_a = np.mean(a1)\n",
    "\n",
    "print(mean_of_a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "855522ae-400c-453c-a5e2-eeeb2a4b4dc7",
   "metadata": {},
   "source": [
    "# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "8d76d459-27e3-4c41-9dbb-5db1191083df",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3628800\n"
     ]
    }
   ],
   "source": [
    "product_of_a = np.product(a1)\n",
    "\n",
    "print(product_of_a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "970dd681-1bd0-4b0f-85e7-bb5b4a4bdc97",
   "metadata": {},
   "source": [
    "# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "814a4e34-82e0-4cea-bcf6-fe9630cd3836",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n"
     ]
    }
   ],
   "source": [
    "square_of_a = [number ** 2 for number in a1]\n",
    "\n",
    "print(square_of_a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71d3d225-5089-42db-b86d-b02ebef10d3e",
   "metadata": {},
   "source": [
    "# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "e024bdb2-f147-4e63-8381-d1f133a57195",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "odds_in_a = [number for number in a1 if number % 2 != 0] \n",
    "            \n",
    "print(odds_in_a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08cab100-0cb4-48db-80b9-11bba6719168",
   "metadata": {},
   "source": [
    "# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "4f2d6260-0adb-4917-bb98-39357bf67ef4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "evens_in_a = [number for number in a1 if number % 2 == 0]\n",
    "\n",
    "print(evens_in_a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1d925e3-6bc4-4d41-9d3b-c338ba6bf72b",
   "metadata": {},
   "source": [
    "## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...\n",
    "## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "89bbccff-954c-4d0a-8508-f2852e787a03",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[3, 4, 5], [6, 7, 8]]\n",
      "[[3 4 5]\n",
      " [6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "b = [\n",
    "    [3, 4, 5],\n",
    "    [6, 7, 8]\n",
    "]\n",
    "\n",
    "ab = np.array(b)\n",
    "\n",
    "\n",
    "print(b)\n",
    "print(ab)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f439b532-3dcf-469d-9350-cdb341f0a535",
   "metadata": {},
   "source": [
    "# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the \"b\" variable is a numpy array**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "1226d1b0-ad20-4ec4-881a-85f9e985b645",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "33\n"
     ]
    }
   ],
   "source": [
    "# sum_of_b = 0\n",
    "# for row in b:\n",
    "#     sum_of_b += sum(row)\n",
    "\n",
    "sum_of_b = np.sum(ab)\n",
    "    \n",
    "    \n",
    "print(sum_of_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c06263b2-e201-405b-941d-e8ef87a66ecd",
   "metadata": {},
   "source": [
    "# Exercise 2 - refactor the following to use numpy. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "e62edd31-5ca3-4c79-87b7-cb5de0858b27",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) \n",
    "\n",
    "min_of_b = np.min(ab)\n",
    "\n",
    "\n",
    "print(min_of_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c63a596-1ffc-4647-9e2d-fa4e4198b8a3",
   "metadata": {},
   "source": [
    "# Exercise 3 - refactor the following maximum calculation to find the answer with numpy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "d085c042-8cb3-4e5c-ab08-2f69f459e0af",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])\n",
    "\n",
    "max_of_b = np.max(ab)\n",
    "\n",
    "print(max_of_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7596527-c449-473e-ac57-3564c5bfcecd",
   "metadata": {},
   "source": [
    "# Exercise 4 - refactor the following using numpy to find the mean of b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "9d23df07-1ea5-40b8-bd2d-936a68c3725f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.5\n"
     ]
    }
   ],
   "source": [
    "# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))\n",
    "\n",
    "mean_of_b = np.mean(ab)\n",
    "\n",
    "print(mean_of_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d89612d-3c3b-44d8-9881-81a70804d54a",
   "metadata": {},
   "source": [
    "# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "9b50fec5-6f02-4c34-b6c0-8347bbde8b5c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20160\n"
     ]
    }
   ],
   "source": [
    "# product_of_b = 1\n",
    "# for row in b:\n",
    "#     for number in row:\n",
    "#         product_of_b *= number\n",
    "\n",
    "product_of_b = np.product(ab)\n",
    "        \n",
    "print(product_of_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "18da9141-3690-49c0-8dbd-d267ae5bdd29",
   "metadata": {},
   "source": [
    "# Exercise 6 - refactor the following to use numpy to find the list of squares "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "31734edb-8c4f-464f-8681-366571fabd98",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 9 16 25]\n",
      " [36 49 64]]\n"
     ]
    }
   ],
   "source": [
    "# squares_of_b = []\n",
    "# for row in b:\n",
    "#     for number in row:\n",
    "#         squares_of_b.append(number**2)\n",
    "\n",
    "squares_of_b = np.square(ab)\n",
    "        \n",
    "print(squares_of_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6f4a067-bbbb-406a-915d-8b9fffd924dc",
   "metadata": {},
   "source": [
    "# Exercise 7 - refactor using numpy to determine the odds_in_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "34499fa1-cc06-4422-b31f-41919dab0ecb",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 5 7]\n"
     ]
    }
   ],
   "source": [
    "# odds_in_b = []\n",
    "# for row in b:\n",
    "#     for number in row:\n",
    "#         if(number % 2 != 0):\n",
    "#             odds_in_b.append(number)\n",
    "\n",
    "odds_in_b = ab[ab % 2 != 0]\n",
    "            \n",
    "print(odds_in_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8299566d-ac32-41e6-b1ea-788a7b73f8ff",
   "metadata": {},
   "source": [
    "# Exercise 8 - refactor the following to use numpy to filter only the even numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "6e7d1b80-a091-407d-b8cb-452b28718b74",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4 6 8]\n"
     ]
    }
   ],
   "source": [
    "# evens_in_b = []\n",
    "# for row in b:\n",
    "#     for number in row:\n",
    "#         if(number % 2 == 0):\n",
    "#             evens_in_b.append(number)\n",
    "\n",
    "evens_in_b = ab[ab % 2 == 0]\n",
    "            \n",
    "print(evens_in_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14ad8725-b66d-46ed-9bab-865cb0703cdc",
   "metadata": {},
   "source": [
    "# Exercise 9 - print out the shape of the array b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "64e6db97-e11f-49b6-986d-af0fb495d707",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# specifying the number of dimensions and the size of each dimension for the array. \n",
    "ab.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72734c1d-e663-4384-88fa-ff02b48a9f09",
   "metadata": {},
   "source": [
    "# Exercise 10 - transpose the array b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "9f672160-2dad-4b4b-8279-c281d71ccbac",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 6],\n",
       "       [4, 7],\n",
       "       [5, 8]])"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.transpose(ab)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "444132c0-8881-41ca-9ff6-9ec068f37fba",
   "metadata": {},
   "source": [
    "# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "89d224ff-3547-4695-8476-55404415e976",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 4, 5, 6, 7, 8]])"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ab.reshape(1,6)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0035afa4-769f-4cc9-8335-8582482d7aaf",
   "metadata": {},
   "source": [
    "# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "2c482e54-2e6c-4888-8a38-7f7125f14bdd",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3],\n",
       "       [4],\n",
       "       [5],\n",
       "       [6],\n",
       "       [7],\n",
       "       [8]])"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ab.reshape(6,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "bc2ddef4-7ae0-4044-a505-35c23cab7f20",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n"
     ]
    }
   ],
   "source": [
    "## Setup 3\n",
    "c = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "\n",
    "c = np.array(c)\n",
    "\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "108c3dfc-9814-4f57-8ade-f4eac29a4d6f",
   "metadata": {},
   "source": [
    "HINT, you'll first need to make sure that the \"c\" variable is a numpy array prior to using numpy array methods.\n",
    "# Exercise 1 - Find the min, max, sum, and product of c."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "7b4e4893-9f3f-44e3-b284-24b68f8ded85",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 9, 45, 362880)"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.min(), c.max(), c.sum(), c.prod()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae3ce700-e1f9-4761-9904-59afcbf54a10",
   "metadata": {},
   "source": [
    "# Exercise 2 - Determine the standard deviation of c."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "917555b3-2d32-4f46-81bd-eb167573e52a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.581988897471611"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.std()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4cc0c6c4-9638-4860-8c89-2fb2725ea8d3",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Exercise 3 - Determine the variance of c."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "5fa5be48-94a7-4b68-b004-3dce8d81ef08",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.666666666666667"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.var()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7fd46ee-9df4-4ef9-a2c0-2aa84ed4d860",
   "metadata": {},
   "source": [
    "# Exercise 4 - Print out the shape of the array c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "57dae8f2-f74b-4544-a287-92da1cd7c1a4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 3)"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.shape "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a085e63-9de5-47b4-8485-b3490d06eefe",
   "metadata": {},
   "source": [
    "# Exercise 5 - Transpose c and print out transposed result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "82ae5d50-2b80-4aa6-96ee-78fb4534fbe5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 8],\n",
       "       [3, 6, 9]])"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(c)\n",
    "\n",
    "c.T"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "928f7931-d0ab-4b1b-b5a5-49a43913d262",
   "metadata": {},
   "source": [
    "# Exercise 6 - Get the dot product of the array c with c. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "f6a318c1-dc93-460f-9045-17fc44583754",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 30,  36,  42],\n",
       "       [ 66,  81,  96],\n",
       "       [102, 126, 150]])"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.dot(c,c)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7cea007-454b-4a67-87ee-c66452c2dcff",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "58adc977-1bfe-4f5e-a7f4-bc4c0e545b3e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  8 21]\n",
      " [ 8 25 48]\n",
      " [21 48 81]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "261"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(c.T * c)\n",
    "\n",
    "(c.T * c).sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d771fce-2bf6-41eb-857e-2c4ea1d74f70",
   "metadata": {},
   "source": [
    "# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "d0fd26a9-9c6f-433c-806d-ac8cc1d70f66",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  8 21]\n",
      " [ 8 25 48]\n",
      " [21 48 81]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "131681894400"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(c.T * c)\n",
    "\n",
    "(c.T * c).prod()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "01514f4d-62a1-4d0d-9cb8-8c3862e0b35e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Setup 4\n",
    "d = [\n",
    "    [90, 30, 45, 0, 120, 180],\n",
    "    [45, -90, -30, 270, 90, 0],\n",
    "    [60, 45, -45, 90, -45, 180]\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bf7396fa-84ca-4f6e-8888-489270fbccad",
   "metadata": {},
   "source": [
    "# Exercise 1 - Find the sine of all the numbers in d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "5db4e9c7-c7f1-4ac1-a5f4-c8e8f730f6a9",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 90  30  45   0 120 180]\n",
      " [ 45 -90 -30 270  90   0]\n",
      " [ 60  45 -45  90 -45 180]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,\n",
       "        -0.80115264],\n",
       "       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,\n",
       "         0.        ],\n",
       "       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,\n",
       "        -0.80115264]])"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = np.array(d)\n",
    "\n",
    "print(d)\n",
    "\n",
    "np.sin(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e391291-2b5f-435e-8104-7786b6dcbd52",
   "metadata": {},
   "source": [
    "# Exercise 2 - Find the cosine of all the numbers in d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "003e6378-aab2-48e6-9857-62907dc0168f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,\n",
       "        -0.59846007],\n",
       "       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,\n",
       "         1.        ],\n",
       "       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,\n",
       "        -0.59846007]])"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.cos(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "737f7a9a-2753-460e-a2ca-2a5e3ccf0ea8",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Exercise 3 - Find the tangent of all the numbers in d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "aec7f595-5ec3-4a84-b5b1-d1fd7414f8d6",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,\n",
       "         1.33869021],\n",
       "       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,\n",
       "         0.        ],\n",
       "       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,\n",
       "         1.33869021]])"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.tan(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "82351a17-4912-4b16-bfc9-8f6264576543",
   "metadata": {},
   "source": [
    "# Exercise 4 - Find all the negative numbers in d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "f7687cca-e1fa-4318-8ab2-50d4e8059b7f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-90, -30, -45, -45])"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d [d < 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "908b55df-f070-42e2-a44b-8bd952e03514",
   "metadata": {},
   "source": [
    "# Exercise 5 - Find all the positive numbers in d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "82ef4c3a-bb0a-46d0-a16e-2afd0a352797",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mask = d > 0\n",
    "\n",
    "d[mask]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8af8e2f1-0ca4-4597-8e0b-8854b3032609",
   "metadata": {},
   "source": [
    "# Exercise 6 - Return an array of only the unique numbers in d."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "fd8a4774-59c4-44a3-a48c-062816f933dc",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b520518c-0ba1-46eb-960b-d4444d1882dd",
   "metadata": {},
   "source": [
    "# Exercise 7 - Determine how many unique numbers there are in d."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "25e226e6-3f59-4bfd-af16-6de215780238",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(np.unique(d))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7183894b-1851-42c8-bfd1-c6489a90faf6",
   "metadata": {},
   "source": [
    "# Exercise 8 - Print out the shape of d."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "4bc80ecb-c4a7-49b1-8bc5-9ed099112f10",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 6)"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0bed0295-66b0-4584-a9b3-94f6c2814df0",
   "metadata": {},
   "source": [
    "# Exercise 9 - Transpose and then print out the shape of d."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "86789cb3-1f9e-4499-a68a-dfcc5707c2e5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(6, 3)\n"
     ]
    }
   ],
   "source": [
    "d.T\n",
    "\n",
    "print(d.T.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31b9d2eb-6186-4198-8c82-f2fb0e007dca",
   "metadata": {},
   "source": [
    "# Exercise 10 - Reshape d into an array of 9 x 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "31192366-fd14-4f4b-b526-c38c2ceb310b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  30],\n",
       "       [ 45,   0],\n",
       "       [120, 180],\n",
       "       [ 45, -90],\n",
       "       [-30, 270],\n",
       "       [ 90,   0],\n",
       "       [ 60,  45],\n",
       "       [-45,  90],\n",
       "       [-45, 180]])"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.reshape(d, (9,2))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
