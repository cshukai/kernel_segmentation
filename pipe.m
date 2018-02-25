img=imread('DSC_0604.NEF')
I = imcrop(img)
originalImage=rgb2gray(I)
thresholdValue = 70; % 30 too little , 50 too large
binaryImage = originalImage > thresholdValue; 
blobMeasurements=regionprops(binaryImage,originalImage,'all')

imshow(originalImage);
axis image; % Make sure image is not artificially stretched because of screen's aspect ratio.
hold on;
boundaries = bwboundaries(binaryImage);
numberOfBoundaries = size(boundaries, 1);
for k = 1 : numberOfBoundaries
	thisBoundary = boundaries{k};
	plot(thisBoundary(:,2), thisBoundary(:,1), 'g', 'LineWidth', 2);
end
hold off;


%crop out
numberOfBlobs = size(blobMeasurements, 1);
    for k = 1 : numberOfBlobs           % Loop through all blobs.
		% Find the bounding box of each blob.
		thisBlobsBoundingBox = blobMeasurements(k).BoundingBox;  % Get list of pixels in current blob.
		% Extract out this coin into it's own image.
		subImage = imcrop(I, thisBlobsBoundingBox);
		filename=strcat('subimage',num2str(k))
		fullname=strcat(filename,'.tiff')
		subimage=imresize(subImage,1000)
        imwrite(subimage,fullname,'tiff')
		% Display the image with informative caption.
		%subplot(100, 3, k);
		%imshow(subImage);

	end