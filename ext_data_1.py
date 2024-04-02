import matplotlib.pyplot as plt

def read_file_and_extract(file_path):
    countries = []
    deaths = []
    
    try:
        with open(file_path, 'r') as file:
            next(file) # Skipping the top line
            for line in file:
                parts = line.strip().split(',')
                country_code = parts[0]
                death_count_str = parts[5].strip('"')  # Remove quotes
                if death_count_str.replace(',', '').isdigit():  # Check if the string contains only digits
                    death_count = float(death_count_str.replace(',', ''))  # Convert to float
                    countries.append(country_code)
                    deaths.append(death_count)
            
        return countries, deaths
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return [], []
        
def draw_scatter_plot(countries, deaths):
    plt.figure(figsize=(10, 6))
    plt.scatter(countries, deaths, color='blue')
    plt.title('Number of Deaths by Country')
    plt.xlabel('Country Code')
    plt.ylabel('Number of Deaths')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
#Example:
file_path = '/Users/ashinwalpola/Documents/XCode/Python/Global Burden of Disease.csv'  # Replace 'data.csv' with the path to your file
countries, deaths = read_file_and_extract(file_path)
draw_scatter_plot(countries, deaths)
    
