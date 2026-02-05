# Introduction

## Data Science vs. Machine Learning

The terms data science and machine learning are often used interchangeably.
Let's explore them to get a better understanding of this course's content.

=== ":bar_chart: Data Science"
    
    **Data Science** is an interdisciplinary field that combines statistics, 
    programming and domain knowledge to extract insights from data. As a data 
    scientist, you could work in vastly different domains, from healthcare and 
    finance to manufacturing and entertainment. The core skills remain the 
    same, but the questions you answer and the data you work with vary greatly.


=== ":robot: Machine Learning"

    **Machine Learning (ML)** is a subset of Data Science that focuses on 
    building algorithms that learn patterns from data to make predictions or 
    decisions.

---

<div style="text-align: center">
    <i>The primary focus of this course is the data science workflow, from 
        setting up your computer to data preparation, exploring different 
        machine learning algorithms to model evaluation.
    </i>
</div>

---

## What to Expect

Before diving into examples and workflows, let's set realistic expectations.

Data science is fundamentally about **understanding and insight**, not 
perfection. You won't find models that are 100% accurate and that's okay - it's
not the goal. Instead, data science helps us:

- **Uncover patterns** in complex data that humans can't easily spot
- **Make informed decisions** based on evidence rather than intuition alone
- **Quantify uncertainty** by understanding where and why models make mistakes
- **Provide actionable insights** that drive business or research value

## Examples

Chances are you've already used services built by data scientists today:

- :material-currency-usd: **Dynamic Pricing**: Airlines and concert platforms 
    adjust prices based on demand, time and user behavior
- :material-movie: **Recommendation Systems**: Netflix suggests movies based 
    on your viewing history; Instagram curates your feed
- :material-email: **Spam Detection**: Your email provider filters unwanted 
    messages automatically

In this course, we'll build models for tasks like:

- :material-home: **Price Prediction**: Estimating house prices based on 
    features like size and location
- :material-hospital: **Medical Diagnosis**: Classifying tumors as malignant or
    benign
- :material-alert: **Anomaly Detection**: Identifying faulty products in 
    manufacturing data

## Building blocks

A typical data science project includes several stages, from collecting raw 
data to deploying models in production. This course focuses on the 
**core workflow**:

<div style="text-align: center">

    ```mermaid
    flowchart TD
        A[Data Collection] --> B[Data Preparation]
        B --> C[Data Preprocessing]
        C --> D[Modeling]
        D --> E[Evaluation]
        E --> F[Deployment]
    ```

</div>

| Stage                  | What You'll Learn                              |
|------------------------|------------------------------------------------|
| **Data Preparation**   | Inspect, clean and structure datasets          |
| **Data Preprocessing** | Transform features (encoding, scaling, etc., ) |
| **Modeling**           | Train different machine learning algorithms    |
| **Evaluation**         | Measure performance and interpret results      |


???+ tip "Iterative Process"

    Data science is rarely linear. You’ll repeatedly cycle through collecting
    data, preparing it, training models and evaluating results. Each evaluation
    highlights new issues (e.g., missing data or unrealistic assumptions) that 
    send you back to earlier stages to improve your approach.

---

Throughout the course, we'll use hands-on Python examples. By the end, you'll 
apply these skills to a complete project from start to finish.

Let's start by setting up your computer for the data science journey.
