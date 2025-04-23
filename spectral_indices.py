import ee

class SpectralIndices:
    def calculate_ndvi(self, image, nir='B8', red='B4'):
        """Calculates the Normalized Difference Vegetation Index (NDVI).

        Args:
            image (ee.Image): The input image.
            nir (str, optional): Name of the near-infrared band. Defaults to 'B8'.
            red (str, optional): Name of the red band. Defaults to 'B4'.

        Returns:
            ee.Image: The NDVI image.
        """
        ndvi = image.normalizedDifference([nir, red]).rename('NDVI')
        return ndvi


    def calculate_ndmi(self, image, nir='B8', swir='B11'):
        """Calculates the Normalized Difference Moisture Index (NDMI).

        Args:
            image (ee.Image): The input image.
            nir (str, optional): Name of the near-infrared band. Defaults to 'B8'.
            swir (str, optional): Name of the shortwave infrared band. Defaults to 'B11'.

        Returns:
            ee.Image: The NDMI image.
        """
        ndmi = image.normalizedDifference([nir, swir]).rename('NDMI')
        return ndmi
    
    
    def calculate_nbr(self, image, nir='B8', swir2='B12'):
        """Calculates the Normalized Burn Ratio (NBR).

        Args:
            image (ee.Image): The input image.
            nir (str, optional): Near-infrared band name. Defaults to 'B8'.
            swir2 (str, optional): Shortwave infrared 2 band name. Defaults to 'B12'.

        Returns:
            ee.Image: The NBR image.
        """
        nbr = image.normalizedDifference([nir, swir2]).rename('NBR')
        return nbr
    

    def calculate_dndvi(self, image1_ndvi, image2_ndvi):
        """Calculates the delta Normalized Difference Vegetation Index (dNDVI)

        Args:
            image1_ndvi (ee.Image): The  NDVI image.
            image2_ndvi (ee.Image): The  NDVI image.

        Returns:
            ee.Image: The dNDVI image.
        """
        dndvi = image1_ndvi.subtract(image2_ndvi).rename('dNDVI')
        return dndvi
    

    def calculate_dndmi(self, image1_ndmi, image2_ndmi):
        """Calculates the delta Normalized Difference Moisture Index (dNDMI).

        Args:
            image1_ndmi (ee.Image): The  NDMI image.
            image2_ndmi (ee.Image): The  NDMI image.

        Returns:
            ee.Image: The dNDMI image.
        """
        dndmi = image1_ndmi.subtract(image2_ndmi).rename('dNDMI')
        return dndmi
    
    
    def calculate_dnbr(self, image1_nbr, image2_nbr, nir='B8', swir2='B12'):
        """Calculates the delta Normalized Burn Ratio (dNBR) from pre- and post-fire images.

        Args:
            image1_nbr (ee.Image): Image before the fire.
            image2_nbr (ee.Image): Image after the fire.
            nir (str, optional): Near-infrared band name. Defaults to 'B8'.
            swir2 (str, optional): Shortwave infrared 2 band name. Defaults to 'B12'.

        Returns:
            ee.Image: The dNBR image.
        """
        
        # Calculate delta NBR
        dnbr = image1_nbr.subtract(image2_nbr).rename('dNBR')
        return dnbr
    

    def process_index(self, image, subregion):
        """Calculate NDVI and NDMI for an image collection over a given subregion.
        Args:
            image (ee.Image): A Sentinel-2 image.
            subregion: A region to calculate mean NDVI/NDMI values within the main image.
            
        """    
        
        # Calculate NDVI
        ndvi = self.calculate_ndvi(image)  # Use your custom NDVI function
        mean_ndvi = ndvi.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=subregion,
            scale=10,
            maxPixels=1e13
        )
        
        # Calculate NDMI
        ndmi = self.calculate_ndmi(image)  # Use your custom NDMI function
        mean_ndmi = ndmi.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=subregion,
            scale=10,
            maxPixels=1e13
        )

        return ee.Feature(None, {
            'date': image.date().format('YYYY-MM-dd'),
            'mean_ndvi': mean_ndvi.get('NDVI'),
            'mean_ndmi': mean_ndmi.get('NDMI')
        })

