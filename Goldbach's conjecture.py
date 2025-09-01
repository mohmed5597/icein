import streamlit as st

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime_sum(num: int):
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i):
            return i, num - i
    return None

st.title("Prime Sum Finder")
num = st.number_input("Enter an even natural number:", min_value=4, step=2)

if num:
    if num % 2 != 0:
        st.warning("Please enter an even number.")
    else:
        pair = find_prime_sum(num)
        if pair:
            st.success(f"{num} = {pair[0]} + {pair[1]}")
        else:
            st.error(f"No prime pair found for {num}")

