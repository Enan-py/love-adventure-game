import streamlit as st

st.title("Tiny Adventure 😏")
st.write("Let's go on a lil date shall we ari?!\n")

# First choice
choice1 = st.radio("Do you want to go to the bed or stay home?", ["Bed", "Home", "Surprise!"])
if choice1:
    if choice1 == "Bed":
        st.write("😳😳🫣 ohh uhh no horny remember???")
    elif choice1 == "Home":
        st.write("Staying in, huh? Cozyy... but you make everything warmer 😏")
    else:
        st.write("Oh a surprise! i wonder what kinda dih is waiting for me😋😋")

# Second choice
choice2 = st.radio("Do you pick ice cream or chocolate?", ["Ice Cream", "Chocolate", "Me"])
if choice2:
    if choice2 == "Ice Cream":
        st.write("Oooh ice cream, that’s sweet… but not as sweet as you 😋🍦")
    elif choice2 == "Chocolate":
        st.write("I think you had a better option down there😔")
    else:
        st.write("😳🫣 ye mommy please eat me🫣")

# Third choice
choice3 = st.radio("Do you want to watch a movie or stargaze?", ["Movie", "Stars", "😏"])
if choice3:
    if choice3 == "Movie":
        st.write("Movie night? Popcorn ready… but I’d rather watch you 😎🎬")
    elif choice3 == "Stars":
        st.write("Stargazing, nice… still can’t compete with your spark! u the besttt ✨")
    else:
        st.write("Ill take that as a baby factory proposal😏")

# Final message
st.write("\nNo matter what you choose in this little adventure…")
st.success("You’re the coolest ever and i wana spend my whole life in your care. Do you... want the same?👉👈. SUPER SORRY IF THIS HIT CRINGE. I TRIED MY BEST😭😭")
