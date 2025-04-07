import pandas as pd

def is_duplicate_product(product_name: str, seen_names: set) -> bool:
    return product_name in seen_names

def is_complete_product(product: dict, required_keys: list) -> bool:
    return all(key in product for key in required_keys)


def custom_modify_data(products: list[dict], key:str='title')->pd.DataFrame:
    """
    Modifies product data by extracting brand names and refining titles.
    
    Args:
        products (list[dict]): List of product dictionaries containing product information
        key (str, optional): Key to extract brand and title from. Defaults to 'title'
        
    Returns:
        pandas df: DataFrame with extracted brand names and refined titles
    """
    brands = [value[key].split(" ")[0] for value in products]
    refined_title = [" ".join(value[key].split(" ")[1:]) for value in products]
    df = pd.DataFrame(products)
    df['brand'] = brands  
    # Reorder columns to have 'brand' first
    cols = ['brand'] + [col for col in df.columns if col != 'brand']
    df = df[cols]  
    df["title"] = refined_title
    return df


def save_products_to_csv(df: pd.DataFrame, filename: str):
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} lights to '{filename}'.")
