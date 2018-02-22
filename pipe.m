img=imread('DSC_0601.NEF')
I = imcrop(img)
originalImage=rgb2gray(I)
thresholdValue = 30; % 30 too little , 50 too large
binaryImage = originalImage > thresholdValue; 
blobMeasurements=regionprops(binaryImage,originalImage,'all')

%crop out
numberOfBlobs = size(blobMeasurements, 1);
    for k = 1 : numberOfBlobs           % Loop through all blobs.
		% Find the bounding box of each blob.
		thisBlobsBoundingBox = blobMeasurements(k).BoundingBox;  % Get list of pixels in current blob.
		% Extract out this coin into it's own image.
		subImage = imcrop(I, thisBlobsBoundingBox);
		filename=strcat('subimage',num2str(k))
		fullname=strcat(filename,'.tiff')
        imwrite(subImage,fullname)
		% Display the image with informative caption.
		%subplot(100, 3, k);
		%imshow(subImage);

	end