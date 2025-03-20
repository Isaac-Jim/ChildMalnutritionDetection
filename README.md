# ChildMalnutritionDetection
### Project Overview  
Malnutrition remains a critical public health issue, particularly in Sub-Saharan Africa, where food insecurity and limited healthcare access are prevalent. This project aims to leverage community-based data to identify children under five at risk of malnutrition, enabling early intervention.  

This notebook documents the data cleaning process,data preprocessing and model building process to ensure reliable analysis and accurate predictions .

## **Dataset Overview**  
This dataset contains key indicators related to malnutrition risk in children under five. It includes child growth metrics, household socioeconomic factors, and access to essential resources to support early intervention efforts.  

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
- **Market Access** – Proximity to food markets (Easy/Moderate/Difficult)  
- **Rural Location** – Whether the household is in a rural area (Yes/No)  

#### **Nutrition & Healthcare**  
- **Frequency of Meals** – Number of meals consumed per day  
- **Dietary Diversity** – Variety of food groups consumed  
- **Breastfeeding Duration (months)** – Duration of exclusive breastfeeding in months  
- **Access to Healthcare** – Availability of healthcare services for the child (Yes/No)  

#### **Living Conditions & Food Security**  
- **Clean Water** – Access to safe drinking water (Yes/No)  
- **Sanitation Facilities** – Quality of sanitation infrastructure (Low/Medium/High)  
- **Availability of Food** – Food security status of the household (Adequate/Inadequate)  
- **Seasonal Variations** – Impact of seasonal changes on food availability (Yes/No)  

#### **Target Variable**  
- **Malnutrition Risk** – Categorized risk level of malnutrition (Low/Moderate/High)  
