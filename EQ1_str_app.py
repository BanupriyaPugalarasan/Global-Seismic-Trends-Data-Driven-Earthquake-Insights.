import streamlit as st
import pymysql
import pandas as pd
conn = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password="Banu@2026sql",
    database="EQ_dataset"

  )
cursor = conn.cursor()
st.set_page_config(layout="wide")
st.markdown(""" <div style ="background-color: linear-gradient(135deg, #2e1065, #581c87, #7e22ce);
            padding:35px;
            border-radius:20px;
            text-align: center;
            box shadow:0px 6px 20px rgba(0,0,0,0.5);
            ">
            <h1 style="colour:#ffffff;
            font-size:48px;
            font-weight :800;
            margin-bottom : 15px;
            ">
            🌍 Global Seismic Trends: Data-Driven Earthquake Insights</h1>
            <p style="
            color:#67e8f9;
            fint-size:40px;
            font-weight :800;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
            ">
            Real - Time Earthquake Insights &
            visualization
            </p>
            </div>""",
            unsafe_allow_html=True
            )

st.image(r"C:\Users\HP\Downloads\noaa-rxlx9Yi0298-unsplash.jpg",
         caption= "Earthquake")

st.header("Earthquake data_set")
query="select * from Earthquake_data"
df=pd.read_sql(query,conn)
st.subheader(" 📌 SQL Query")
st.code(query, language='sql')
st.subheader(" 📊 Query Output")
st.dataframe(df)
st.success(" Query executed successfully ✅")

questions = ["1.Top 10 strongest earthquakes(mag)",
             "2.Top 10 deepest eqrthquakes(depth_km)",
             "3.Shallow earthquake <50 km and mag>7.5",
             "4.Average depth per continent",
             "5.Average magnitude per magnitude type(magType)",
             "6.Year with most earthquakes",
             "7.Month with Highest number of earthquakes",
             "8.Day of week with most earthquakes",
             "9.Count of earthquakes per hour of day",
             "10.Most active reporting network(net)",
             "11.Top 5 places with highest Casualties",
             "12.Total estimated economic loss per continent",           
             "13.Average economic loss by alert level",
             "14.Count of reviewed vs automatic earthquakes(status)",
             "15.Count by earthquake type",
             "16.Number of earthquakes by data type(types)",
             "17.Average RMS and gap per continent",
             "18.Events with high station coverage(nst>thresold)",
             "19. Number of Tsunamis triggered per year",
             "20.Count earthquakes by alert levels(red,Orange,etc)",
             "21.Find the top 5 countries with the highest average magnitude of earthquakes in the past 5 years",
             "22.Find countries that have experienced both shallow and deep earthquakes within the same month",
             "23.Compute the year-over-year growth rate in the total number of earthquakes globally",
             "24.List the 3 most seismically active regions by combining both frequency and average magnitude",
             "25.For each country, calculate the average depth of earthquakes within ±5° latitude range of the equator",
             "26.Identify countries having the highest ratio of shallow to deep earthquakes",
             "27.Find the average magnitude difference between earthquakes with tsunami alerts and those without",
             "28.Using the gap and rms columns, identify events with the lowest data reliability (highest average error margins)",
             "29.Find pairs of consecutive earthquakes (by time) that occurred within 50 km of each other and within 1 hour",
             "30.Determine the regions with the highest frequency of deep-focus earthquakes (depth > 300 km)"
             ]     
    
  
st.header("Analyst Tasks")

query=st.selectbox("**Select your questions**",questions)

if query == "1.Top 10 strongest earthquakes(mag)":
    Q1="""SELECT id,place,mag 
              FROM earthquake_data  
              ORDER BY mag DESC
              LIMIT 10; """     
    df1=pd.read_sql(Q1,conn)
    st.subheader(" 📌 SQL Query")
    st.code(query, language='sql')
    st.subheader(" 📊 Query Output")
    st.dataframe(df1)
    st.success(" Query executed successfully ✅")


elif query =="2.Top 10 deepest eqrthquakes(depth_km)":
  Q2="""SELECT place,mag,depth_km
        FROM earthquake_data
        ORDER BY depth_km DESC
        LIMIT 10; """
  df2=pd.read_sql(Q2,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df2)
  st.success(" Query executed successfully ✅")

elif query == "3.Shallow earthquake <50 km and mag>7.5":
  Q3="""SELECT place, depth_km,mag,earthquake_flag 
          FROM earthquake_data
          WHERE depth_km<50 And mag>7.5"""
  df3=pd.read_sql(Q3,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df3)
  st.success(" Query executed successfully ✅")

elif query=="4.Average depth per continent": 
  st.write("Answer Unavailable:'Continent column is not present in the dataset")

elif query == "5.Average magnitude per magnitude type(magType)":
  Q5="""SELECT magType,AVG(mag) AS AVERAGE_MAG
               FROM earthquake_data
               GROUP BY magType"""
  df5=pd.read_sql(Q5,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df5)
  st.success(" Query executed successfully ✅")

elif query == "6.Year with most earthquakes":
  Q6="""SELECT year,count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY year
               ORDER BY total_earthquakes DESC
               Limit 1;"""
  df6=pd.read_sql(Q6,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df6)
  st.success(" Query executed successfully ✅")

elif query =="7.Month with Highest number of earthquakes":
  Q7="""SELECT month, count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY month
               ORDER BY total_earthquakes DESC
               LIMIT 1;"""
  df7=pd.read_sql(Q7,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df7)
  st.success(" Query executed successfully ✅")

elif query =="8.Day of week with most earthquakes":
  Q8="""SELECT day_of_week, count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY day_of_week
               ORDER BY total_earthquakes DESC
               LIMIT 1;"""
  df8=pd.read_sql(Q8,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df8)
  st.success(" Query executed successfully ✅")

elif query == "9.Count of earthquakes per hour of day":
  Q9="""SELECT hour(time) AS hour_of_day, count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY hour_of_day
               ORDER BY total_earthquakes DESC
               ;"""
  df9=pd.read_sql(Q9,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df9)
  st.success(" Query executed successfully ✅")

elif query== "10.Most active reporting network(net)":
  Q10="""SELECT net, count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY net
               ORDER BY total_earthquakes DESC
               LIMIT 1;"""
  df10=pd.read_sql(Q10,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df10)
  st.success(" Query executed successfully ✅")

elif query =="11.Top 5 places with highest Casualties":
  Q11="""SELECT place, Max(felt) AS highest_casualties
               FROM earthquake_data
               GROUP BY place
               ORDER BY highest_casualties DESC
               LIMIT 5;"""
  df11=pd.read_sql(Q11,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df11)
  st.success(" Query executed successfully ✅")

elif query=="12.Total estimated economic loss per continent":
  st.write("Answer Unavailable:'Continent column is not present in the dataset")

elif query == "13.Average economic loss by alert level":
  Q13 ="""SELECT alert,Avg(mag) AS Average_eco_loss
               FROM earthquake_data
               GROUP BY alert;"""
  df13=pd.read_sql(Q13,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df13)
  st.success(" Query executed successfully ✅")

elif query == "14.Count of reviewed vs automatic earthquakes(status)":
  Q14 ="""SELECT status,count(*) AS Total_Earthquakes
               FROM earthquake_data
               GROUP BY status;"""
  df14=pd.read_sql(Q14,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df14)
  st.success(" Query executed successfully ✅")

elif query == "15.Count by earthquake type":
  Q15="""SELECT type,count(*) AS Total_Earthquakes
               FROM earthquake_data
               GROUP BY type;"""
  df15=pd.read_sql(Q15,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df15)
  st.success(" Query executed successfully ✅")

elif query == "16.Number of earthquakes by data type(types)":
  Q16="""SELECT types,count(*) AS Number_of_Earthquakes
               FROM earthquake_data
               GROUP BY types;"""
  df16=pd.read_sql(Q16,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df16)
  st.success(" Query executed successfully ✅")

elif query=="17.Average RMS and gap per continent":
  st.write("Answer Unavailable:'Continent column is not present in the dataset")

elif query =="18.Events with high station coverage(nst>thresold)":
  Q18="""SELECT id,mag,mag_flag,nst
               FROM earthquake_data
               WHERE nst>mag
               ORDER BY nst DESC;"""
  df18=pd.read_sql(Q18,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df18)
  st.success(" Query executed successfully ✅")

elif query =="19. Number of Tsunamis triggered per year":
  Q19="""SELECT year,tsunami,count(*) AS Total_earthquakes
               FROM earthquake_data
               WHERE tsunami =1
               GROUP BY year
               ORDER BY Total_earthquakes DESC;"""
  df19=pd.read_sql(Q19,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df19)
  st.success(" Query executed successfully ✅")

elif query =="20.Count earthquakes by alert levels(red,Orange,etc)":
  Q20="""SELECT alert,count(*) AS Total_earthquakes
               FROM earthquake_data
               GROUP BY alert
               ORDER BY Total_earthquakes DESC;"""
  df20=pd.read_sql(Q20,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df20)
  st.success(" Query executed successfully ✅")

elif query =="21.Find the top 5 countries with the highest average magnitude of earthquakes in the past 5 years":
  Q21="""SELECT place,AVG(mag) AS Avarage_magnitude
               FROM earthquake_data
               GROUP BY place
               ORDER BY Avarage_magnitude DESC
               LIMIT 5;"""
  df21=pd.read_sql(Q21,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df21)
  st.success(" Query executed successfully ✅")

elif query =="22.Find countries that have experienced both shallow and deep earthquakes within the same month":
  Q22="""SELECT place
               FROM earthquake_data
               GROUP BY place, month
               HAVING SUM(CASE WHEN earthquake_flag = "shallow" THEN 1 ELSE 0 END)>0 
               AND SUM(CASE WHEN earthquake_flag = "deep" THEN 1 ELSE 0 END)>0;
               """
  df22=pd.read_sql(Q22,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df22)
  st.success(" Query executed successfully ✅")

elif query=="23.Compute the year-over-year growth rate in the total number of earthquakes globally":
  Q23=""" SELECT
               year,
               total_earthquake,

               LAG(total_earthquake) OVER (ORDER BY year) AS prev_year_earthquake,
               ROUND(
               (
               (total_earthquake-LAG(total_earthquake) OVER (ORDER BY year))*100.0 /
               LAG(total_earthquake) OVER(ORDER BY year)
               ),
               2 ) AS yoy_growth_rate

               FROM (SELECT year,
               COUNT(*) AS total_earthquake
               FROM earthquake_data
               GROUP BY year) AS yearly;
               """
  df23=pd.read_sql(Q23,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df23)
  st.success(" Query executed successfully ✅")

elif query =="24.List the 3 most seismically active regions by combining both frequency and average magnitude":
  Q24="""SELECT place,
               COUNT(*) AS frequency,
               AVG(mag) AS Avg_magnitude
               FROM earthquake_data
               GROUP BY place
               ORDER BY frequency DESC, Avg_magnitude DESC
               LIMIT 3;"""
  df24=pd.read_sql(Q24,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df24)
  st.success(" Query executed successfully ✅")

elif query =="25.For each country, calculate the average depth of earthquakes within ±5° latitude range of the equator":
  Q25="""SELECT place, AVG(depth_km) AS Avg_depth_km
               FROM earthquake_data
               WHERE latitude  between -5 and +5
               GROUP BY place;
               """
  df25=pd.read_sql(Q25,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df25)
  st.success(" Query executed successfully ✅")

elif query=="26.Identify countries having the highest ratio of shallow to deep earthquakes":
  Q26="""SELECT place,
               SUM(CASE WHEN earthquake_flag = "shallow" THEN 1 ELSE 0 END) AS shallow_count,
               SUM(CASE WHEN earthquake_flag = "deep"THEN 1 ELSE 0 END) AS deep_count,
               SUM(CASE WHEN earthquake_flag = "shallow" THEN 1 ELSE 0 END) *1.0 /
               NULLIF(SUM(CASE WHEN earthquake_flag = "deep"THEN 1 ELSE 0 END),0) AS ratio
               FROM earthquake_data
               GROUP BY place
               ORDER BY ratio DESC;"""
  df26=pd.read_sql(Q26,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df26)
  st.success(" Query executed successfully ✅")

elif query =="27.Find the average magnitude difference between earthquakes with tsunami alerts and those without":
  Q27="""SELECT
               AVG(CASE WHEN tsunami = 1 THEN mag END) -
               AVG(CASE WHEN tsunami = 0 THEN mag END) AS avg_magnitude_difference
               FROM earthquake_data;"""
  df27=pd.read_sql(Q27,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df27)
  st.success(" Query executed successfully ✅")

elif query=="28.Using the gap and rms columns, identify events with the lowest data reliability (highest average error margins)":
  Q28="""SELECT id,
               place,
               gap,
               rms
               FROM earthquake_data
               ORDER BY gap DESC,rms DESC
               LIMIT 1;"""
  df28=pd.read_sql(Q28,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df28)
  st.success(" Query executed successfully ✅")

elif query == "29.Find pairs of consecutive earthquakes (by time) that occurred within 50 km of each other and within 1 hour":
  st.write("Answer Unavailable")

elif query=="30.Determine the regions with the highest frequency of deep-focus earthquakes (depth > 300 km)":
  Q30="""SELECT place,count(*) AS frequency
               FROM earthquake_data
               WHERE depth_km>300
               GROUP BY place
               ORDER BY frequency DESC
               LIMIT 1;"""
  df30=pd.read_sql(Q30,conn)
  st.subheader(" 📌 SQL Query")
  st.code(query, language='sql')
  st.subheader(" 📊 Query Output")
  st.dataframe(df30)
  st.success(" Query executed successfully ✅")

if st.checkbox("Finish Project"):
  st.balloons()
  st.success(" 🎉 Project Completed Successfully! 🥳 ")
  st.info("All SQL analysis done📊")
  st.write("🙏 Thank you fou using the dashboard 🙏")
