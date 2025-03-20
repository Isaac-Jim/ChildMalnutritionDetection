# ChildMalnutritionDetection
## Project Overview  
Malnutrition remains a critical public health issue, particularly in Sub-Saharan Africa, where food insecurity and limited healthcare access are prevalent. This project aims to leverage community-based data to identify children under five at risk of malnutrition, enabling early intervention.  

This notebook documents the data cleaning process,data preprocessing and model building process to ensure reliable analysis and accurate predictions .

## **Dataset Overview**  
This dataset contains key indicators related to malnutrition risk in children under five. It includes child growth metrics, household socioeconomic factors, and access to essential resources to support early intervention efforts.  
1 means yes , 0 means no

### **Key Features**  

#### **Child Characteristics**  
- **Gender** – Sex of the child (Male/Female)  
- **Birth Order** – Position of the child in the family (e.g., firstborn, second-born)  
- **Weight-for-Age** – Standardized weight measurement based on age  
- **Height-for-Age** – Standardized height measurement based on age  
- **Weight-for-Height** – Standardized weight measurement based on height  

#### **Household & Socioeconomic Factors**  
- **Family Size** – Total number of household members  
- **Parental Education** – Educational attainment of parents  
- **Household Income (₦)** – Monthly income of the household in Nigerian Naira  
- **Market Access** – Proximity to food markets (1/0)  
- **Rural Location** – has the rural location   

#### **Nutrition & Healthcare**  
- **Frequency of Meals** – Number of meals consumed per day  
- **Dietary Diversity** – Variety of food groups consumed  
- **Breastfeeding Duration (months)** – Duration of exclusive breastfeeding in months  
- **Access to Healthcare** – Availability of healthcare services for the child (1/0)  

#### **Living Conditions & Food Security**  
- **Clean Water** – Access to safe drinking water (1/0)  
- **Sanitation Facilities** – Quality of sanitation infrastructure (1/0)  
- **Availability of Food** – Food security status of the household (1/0)  
- **Seasonal Variations** – Impact of seasonal changes on food availability (1/0)  

#### **Target Variable**  
- **Malnutrition Risk** – Categorized risk level of malnutrition (Low/Moderate/High)  
