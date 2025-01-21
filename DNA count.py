{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "99cc5dc0-6e0e-4de1-9153-18c102c11032",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import altair as alt\n",
    "import streamlit as st\n",
    "\n",
    "# Sample data for demonstration purposes\n",
    "# Replace this with your actual dataset\n",
    "data = {\n",
    "    \"nucleotide\": [\"A\", \"T\", \"C\", \"G\", \"A\", \"T\", \"C\", \"G\"],\n",
    "    \"count\": [5, 10, 15, 20, 10, 15, 5, 10]\n",
    "}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Verify that required columns exist in the dataframe\n",
    "required_columns = [\"nucleotide\", \"count\"]\n",
    "for col in required_columns:\n",
    "    if col not in df.columns:\n",
    "        st.error(f\"Missing required column: {col}\")\n",
    "        st.stop()\n",
    "\n",
    "# Create the Altair chart\n",
    "try:\n",
    "    chart = (\n",
    "        alt.Chart(df)\n",
    "        .mark_bar()\n",
    "        .encode(\n",
    "            x=alt.X(\"nucleotide:O\", title=\"Nucleotide\"),\n",
    "            y=alt.Y(\"count:Q\", title=\"Count\"),\n",
    "            color=alt.Color(\"nucleotide:O\", legend=None),\n",
    "            tooltip=[\"nucleotide\", \"count\"]\n",
    "        )\n",
    "        .properties(\n",
    "            width=alt.Step(80),  # Step size for bar width\n",
    "            height=300,\n",
    "            title=\"Nucleotide Count Bar Chart\"\n",
    "        )\n",
    "    )\n",
    "    st.altair_chart(chart, use_container_width=True)\n",
    "except Exception as e:\n",
    "    st.error(f\"An error occurred while creating the chart: {e}\")\n",
    "\n",
    "# Additional debugging information\n",
    "st.write(\"### Data Preview\")\n",
    "st.dataframe(df)"
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
