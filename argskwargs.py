{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def color(red,blue,green,**kwargs):\n",
    "    print('r =',red)\n",
    "    print('b =', blue)\n",
    "    print('g =',green)\n",
    "    print(kwargs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "r = 32\n",
      "b = 67\n",
      "g = 60\n",
      "{'alpha': 100, 'beta': 30}\n"
     ]
    }
   ],
   "source": [
    "kcolor = {'red': 32, 'blue': 67, 'green': 60, 'alpha': 100, 'beta': 30}\n",
    "color(**kcolor)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "r = 2\n",
      "b = 3\n",
      "g = 4\n",
      "{'merun': 70, 'yellow': 80}\n"
     ]
    }
   ],
   "source": [
    "color(2,3,4,merun=70,yellow=80)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "r = 2\n",
      "b = 3\n",
      "g = 4\n",
      "{'redu': 32, 'bluee': 67, 'greene': 60, 'alpha': 100, 'beta': 30}\n"
     ]
    }
   ],
   "source": [
    "kcolor = {'redu': 32, 'bluee': 67, 'greene': 60, 'alpha': 100, 'beta': 30}\n",
    "color(2,3,4,**kcolor)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'red': 30, 'blue': 50, 'green': 60, 'alpha': 100, 'beta': 90}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k =dict(red= 30, blue= 50, green= 60, alpha= 100, beta = 90)\n",
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "def trace(func,*args,**kwargs): # extended formal argument syntax\n",
    "    print(\"args = \",args)\n",
    "    print(\"kwargs = \",kwargs)\n",
    "    result = func(*args, **kwargs) # extended call syntax for positional arbitrary arguments and keyword args\n",
    "    print(\"result = \", result)\n",
    "    return result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "255"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(\"ff\", base=16)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "args =  ('ff',)\n",
      "kwargs =  {'base': 16}\n",
      "result =  255\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "255"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "trace(int,\"ff\", base=16)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
