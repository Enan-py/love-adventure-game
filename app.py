import streamlit as st

st.title("Tiny Adventure 😏")
st.write("Let's go on a tiny adventure together!\n")

# First choice
choice1 = st.radio("Do you want to go to the park or stay home?", ["Park", "Home", "Surprise!"])
if choice1:
    if choice1 == "Park":
        st.write("Oooh the park, nice! But still not as fresh as you 🌞")
    elif choice1 == "Home":
        st.write("Staying in, huh? Cozy vibes… but you make everything warmer 😏")
    else:
        st.write("Hmm, a mystery move! Just like your vibe 😎")

# Second choice
choice2 = st.radio("Do you pick ice cream or chocolate?", ["Ice Cream", "Chocolate", "Mystery Snack"])
if choice2:
    if choice2 == "Ice Cream":
        st.write("Oooh ice cream, that’s sweet… but not as sweet as you 😋🍦")
    elif choice2 == "Chocolate":
        st.write("Chocolate huh? Dark and smooth… kinda like you 😏🍫")
    else:
        st.write("A surprise snack! Just like how you surprise me 😄")

# Third choice
choice3 = st.radio("Do you want to watch a movie or stargaze?", ["Movie", "Stars", "Unexpected"])
if choice3:
    if choice3 == "Movie":
        st.write("Movie night? Popcorn ready… but I’d rather watch you 😎🎬")
    elif choice3 == "Stars":
        st.write("Stargazing, nice… still can’t compete with your sparkle ✨")
    else:
        st.write("Unexpected plans! I like that… keeps me on my toes 😏")

# Final message
st.write("\nNo matter what you choose in this little adventure…")
st.success("You’re amazing 😘 And I’m lucky to have you in my world ❤️")