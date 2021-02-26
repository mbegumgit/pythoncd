{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['aze']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['ada', 'bbb', 'abc', 'aze']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "store =[]\n",
    "def sort_by_lastletter(strings):\n",
    "    def last_letter(s):\n",
    "        return s[-1]\n",
    "    store.append(last_letter(strings))\n",
    "    print(store)\n",
    "    return sorted(strings, key=last_letter)\n",
    "data=['abc','ada', 'bbb','aze']\n",
    "sort_by_lastletter(data)"
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
