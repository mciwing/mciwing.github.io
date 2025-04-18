# Building Web Applications with Streamlit

## Introduction

<figure markdown="span">
  ![Streamlit Logo](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-lighttext.svg){ width="250" }
</figure>


As the final topic in our `Python` :fontawesome-brands-python: course, we introduce `streamlit`, 
a powerful framework for building web applications. It allows you to turn your Python scripts into 
interactive web apps with minimal effort, handling most of the complexities of web development in the background. This knowledge will prove invaluable when showcasing your data analysis or machine learning projects.

???+ info

    At the time of writing, `streamlit` version `1.41.0` was used. Keep in mind that
    `streamlit` is actively developed and some functionalities might change in the future.
    However, as always, we try to keep the content up-to-date.

    This section is based on the excellent [Streamlit documentation](https://docs.streamlit.io).

---

## Prerequisites

For this section, it's best to create a new project folder and a fresh **virtual environment**, then **activate** it. 
Refer back to the [packages and virtual environments](packages.md) section if you need a refresher. Next, create a file named `app.py`.

You should end up with a project structure similar to the following:

```
📁 streamlit/
├── 📁 .venv/
└── 📄 app.py
```

Finaly, install `streamlit`:

```bash
pip install streamlit
```

To verify the installation, run:

```bash
streamlit hello
```

This command launches Streamlit's built-in demo app in your default web browser. To stop the app, go back to the terminal window and press: ++ctrl+c++.

???+ info "Switch from Jupyter to standalone Python?"
    Up until now, we’ve primarily used Jupyter Notebooks (`.ipynb`) for experimentation and data analysis. However, to build shareable, user-friendly applications, standalone Python scripts (`.py`) are typically more suitable. Streamlit enables you to create interactive web apps directly from Python files, adding a professional edge and new level of interactivity to your projects.

## Your First Streamlit App

Let’s create a basic Streamlit application. In app.py, add the following code:

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to Streamlit!")
```

To run the app, execute the following command in your terminal:

```bash
streamlit run app.py
```

Streamlit will open a new tab in your web browser and display your app.

???+ info "Hot Reloading"
    Streamlit automatically detects changes in your source code and updates the web 
    application in real time. If you notice the hot reloading feature isn’t working as expected, use the "Rerun" button in the upper-right corner of the Streamlit app or enable the "Always rerun" option.

## Basic Elements

Streamlit provides various elements to build your web interface. Let's explore some of the most 
commonly used ones.

### Text Elements

```python
import streamlit as st

# Display text
st.title("Main Title")
st.header("Header")
st.subheader("Subheader")
st.text("Simple text")
st.markdown("**Bold** and *italic* text")

# Information boxes
st.info("Info message")
st.warning("Warning message")
st.error("Error message")
st.success("Success message")
```

### Input Widgets

Streamlit offers multiple widgets for capturing user input:

```python
# Text input
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

# Numeric input
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)

# Slider
temperature = st.slider("Select temperature", min_value=-10.0, max_value=40.0, value=20.0)

# Checkbox
agree = st.checkbox("I agree to the terms")
if agree:
    st.write("Thank you for agreeing!")

# Select box
option = st.selectbox(
    "What's your favorite color?",
    ["Red", "Green", "Blue"]
)
```

???+ question "Temperature Converter"
    
    Create a simple temperature converter application that:
    
    1. Accepts temperature input in Celsius via `st.number_input`
    2. Converts this temperature to Fahrenheit using °F = (°C × 9/5) + 32
    3. Displays the result with `st.write`
    
    <blockquote class="reddit-embed-bq" style="height:400px" data-embed-height="593"><a href="https://www.reddit.com/r/memes/comments/sqm4wh/the_ultimate_temperature_conversion_guide/">The Ultimate temperature conversion guide....</a><br> by<a href="https://www.reddit.com/user/noobmaster69_is_hela/">u/noobmaster69_is_hela</a> in<a href="https://www.reddit.com/r/memes/">memes</a></blockquote><script async="" src="https://embed.reddit.com/widgets.js" charset="UTF-8"></script>

### Data Display

Streamlit makes it easy to display `pandas` dataframes and other data structures:

```python
import streamlit as st
import pandas as pd
import numpy as np

# Create sample data
data = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 22, 35],
    'City': ['New York', 'Paris', 'London']
})

# Display data
st.dataframe(data)  # Interactive dataframe
st.table(data)      # Static table
```

Furthermore, Streamlit allows us to edit dataframe right in the application: 

```python
# Display data and allow user to edit it
edited_table = st.data_editor(data)

oldest_name = edited_table.loc[edited_table["Age"].idxmax()]["Name"]
st.markdown(f"The oldest Person is **{oldest_name}** 🎈")
```


### Charts and Plots

Streamlit seamlessly integrates with plotting libraries such as Matplotlib, Seaborn, or Plotly (make sure to install these libraries first).

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# Seaborn
sns.set_theme()
tips = sns.load_dataset("tips")
fig = plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip")
st.pyplot(fig)
```

???+ info "Interactive Plots"

    Streamlit also supports interactive plotting libraries like Plotly:
    
    ```python
    import plotly.express as px
    
    fig = px.scatter(tips, x="total_bill", y="tip", color="size")
    st.plotly_chart(fig)
    ```

## Layout and Containers

Streamlit provides several options to manage your layout and organize the user interface.

### Columns

```python
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is the first column")

with col2:
    st.header("Column 2")
    st.write("This is the second column")
```

### Tabs

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.header("Tab 1 Content")
    st.write("This is the first tab")

with tab2:
    st.header("Tab 2 Content")
    st.write("This is the second tab")
```

### Expanders

```python
with st.expander("Click to expand"):
    st.write("This content is hidden by default")
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7d/Seal_point_Sphynx_Kitten.jpg")
```


???+ info "Did You Know?"

    Streamlit automatically adjusts its layout to fit different screen sizes, ensuring your app looks great on both desktop and mobile devices.


## File Upload and Download

Streamlit makes it easy to handle file uploads and downloads:

```python
# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# File download
st.download_button(
    label="Download data as CSV",
    data=data.to_csv(index=False),
    file_name='sample_data.csv',
    mime='text/csv',
)
```

???+ question "CSV Data Analyzer"
    
    Create a Streamlit application that:
    
    1. Lets users upload the 'Student Data' CSV file from [before](data/tabular.md#reading-excel-files)
    2. Displays basic statistics using `df.describe()`
    3. Creates a line chart based on the 'Student Data' dataset using ploty and visualize it in the streamlit application
    
    Bonus: Add error handling for invalid file formats and empty data frames.

## Optional: Session State

Streamlit is stateless by default, meaning it reruns your entire script on any user interaction. 
Session state allows you to persist data between reruns:

```python
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('Increment'):
    st.session_state.counter += 1

st.write('Counter:', st.session_state.counter)
```

???+ info "When to Use Session State"

    Use session state when you need to:

    - Persist data between reruns
    - Share data between different parts of your app
    - Implement counters or progress tracking
    - Store user preferences

## Best Practices

1. **Performance**
    - Cache expensive computations using `@st.cache_data`
    - Use appropriate container widgets to organize your layout
    - Minimize the use of heavy computations in the main thread

2. **User Experience**
    - Add proper error handling
    - Include loading indicators for long operations
    - Provide clear instructions and feedback
    - Use appropriate input validation

3. **Code Organization**
    - Split your code into logical functions
    - Use config files for constants
    - Follow Python naming conventions

## Example: Data Dashboard

Let's create a simple dashboard that combines various Streamlit features:

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

# Page config
st.set_page_config(page_title="Data Dashboard", layout="wide")

# Title
st.title("📊 Data Dashboard")

# Sidebar
st.sidebar.header("Settings")
dataset = st.sidebar.selectbox(
    "Select Dataset",
    ["Iris", "Diamonds", "Tips"]
)

# Load data
@st.cache_data
def load_data(dataset_name):
    if dataset_name == "Iris":
        return sns.load_dataset("iris")
    elif dataset_name == "Diamonds":
        return sns.load_dataset("diamonds")
    else:
        return sns.load_dataset("tips")

data = load_data(dataset)

# Display data overview
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Preview")
    st.dataframe(data.head())

with col2:
    st.subheader("Basic Statistics")
    st.dataframe(data.describe())

# Visualizations
st.subheader("Data Visualization")
tab1, tab2 = st.tabs(["Distribution", "Relationships"])

with tab1:
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    col = st.selectbox("Select Column", numeric_cols)
    fig = px.histogram(data, x=col)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    x_col = st.selectbox("Select X axis", numeric_cols, key="x")
    y_col = st.selectbox("Select Y axis", numeric_cols, key="y")
    fig = px.scatter(data, x=x_col, y=y_col)
    st.plotly_chart(fig, use_container_width=True)
```

## Deployment

Streamlit applications can be deployed in various ways:

1. **Streamlit Cloud** (Recommended for small projects) [:octicons-link-external-16:](https://docs.streamlit.io/deploy/streamlit-community-cloud)
    - Push your code to a GitHub repository.
    - Log in to [Streamlit Cloud](https://streamlit.io/cloud).
    - Connect your repository and deploy the app.

2. **Docker** [:octicons-link-external-16:](https://docs.streamlit.io/deploy/tutorials/docker)

3. **Kubernetes** [:octicons-link-external-16:](https://docs.streamlit.io/deploy/tutorials/kubernetes)

???+ info "Production Deployment"

    When deploying to production:

    - Use requirements.txt or Poetry for dependency management
    - Set up proper environment variables
    - Configure authentication if needed
    - Monitor application performance
    - Set up error logging

## Recap

In this chapter, we covered the fundamentals of building web applications with Streamlit. We 
explored:

- Basic Streamlit elements and widgets
- Data visualization and interaction
- Layout management
- File handling
- Session state
- Best practices
- Deployment options

With these skills, you can now transform your Python scripts into interactive web applications 
that can be shared with others.

???+ info "🎉"
    
    Congratulations! You've completed the Streamlit chapter. You're now equipped to create
    interactive web applications using Python.
    
    <figure markdown="span">
      ![Celebration](https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/giphy.gif){ width="350" }
    </figure>