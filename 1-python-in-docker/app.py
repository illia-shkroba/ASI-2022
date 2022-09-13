import pandas as pd
import streamlit as st
from data_processor.case import camel2snake
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

title = "Camel2Snake normalizer"
st.set_page_config(page_title=title)
st.title(title)

(file_uploader,) = st.columns([6])

with file_uploader:
    uploaded_file = st.file_uploader(label="")

    if uploaded_file is not None:
        file_container = st.expander("Check your uploaded CSV")
        uploaded_df = pd.read_csv(uploaded_file)
        uploaded_file.seek(0)
        file_container.write(uploaded_df)
    else:
        st.info("Upload a CSV file first.")
        st.stop()

selected_columns = st.multiselect(
    label="Columns", options=uploaded_df.columns[uploaded_df.dtypes == object]
)

gb = GridOptionsBuilder.from_dataframe(uploaded_df)
gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_side_bar()
gridOptions = gb.build()
response = AgGrid(
    uploaded_df,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    fit_columns_on_grid_load=False,
)

df = pd.DataFrame(response["selected_rows"])

if df.empty:
    st.stop()

df = df.loc[:, uploaded_df.columns]
df.loc[:, selected_columns] = df.loc[:, selected_columns].apply(
    lambda xs: xs.apply(camel2snake), axis="columns"
)

st.success("Normalized data 👇")
st.table(df)

st.download_button(
    label="Download normalized data as CSV",
    data=df.to_csv(index=False),
    file_name="normalized.csv",
)
st.download_button(
    label="Download normalized data as JSON",
    data=df.to_json(orient="records"),
    file_name="normalized.json",
)
