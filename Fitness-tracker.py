import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

names = ['Rejoice','Aravind','Madhan','Kalyan','Kartik','Harshith','Jayanth']
steps = np.random.randint(4000, 30000,size=7)
sleep = np.round(np.random.uniform(4.5,10.5,size=7),1)
calories = np.random.randint(1500,4000,size=7)


df = pd.DataFrame({
    'Name':names,
    'Steps':steps,
    'Sleep':sleep,
    'Calories':calories,
    })

df['HealthScore'] = np.round(
      (df['Steps']/30000)*0.5 +
      (df['Sleep']/10)*0.3 +
      (df['Calories']/4000)*0.3,2
)

print(df)


plt.figure(figsize=(10,5))
plt.bar(df['Name'], df['HealthScore'])
plt.title('Weekly Health Score Per Person',color='#000000',fontsize=20)
plt.xlabel('Name',color='#000000',fontsize=15)
plt.ylabel('Health Score',color='#000000',fontsize=15)
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('health_score_plot.png')
plt.show()



plt.pie(df['HealthScore'], labels=df['Name'], autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Health Score Distribution',color='#00FFFF',fontsize=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('health_score_distribution.png')
plt.show()