%%%%%%%%%%%%%%%%%color thresholding approach###################
img=imread('DSC_0604.NEF')

I = imcrop(img)
originalImage=rgb2gray(I)
thresholdValue = 130; % 30 too little , 50 too large
binaryImage = originalImage > thresholdValue; 


%remove small object representing kernels in blue/purple
BW2 = bwareaopen(binaryImage, 3);

 subplot(4,1,1)
 imshow(binaryImage)
 subplot(4,1,2)
 imshow(BW2)

%blobMeasurements=regionprops(binaryImage,originalImage,'all')
blobMeasurements=regionprops(BW2,originalImage,'all')



% test if the bounding boxes are correctly located
subplot(4,1,3)
imshow(originalImage);
axis image; % Make sure image is not artificially stretched because of screen's aspect ratio.

hold on;
boundaries = bwboundaries(binaryImage);
numberOfBoundaries = size(boundaries, 1);

for k = 1 : numberOfBoundaries
	thisBoundary = boundaries{k};
	plot(thisBoundary(:,2), thisBoundary(:,1), 'g', 'LineWidth', 1);
	
end
hold off;
 subplot(4,1,4)
 imshow(I)

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


%%%%%%%%%%%%%%%%%%%%%%%%%%background-substraction-based approach%%%%%%%%%%%
img=imread('DSC_0604.NEF')
fore = double(img)/255;
back = double(imread('DSC_0725.NEF'))/255;
out=fore-back
I = imcrop(out)
originalImage=rgb2gray(I)

thresholdValue = 0.0001; % 30 too little , 50 too large
BW = originalImage > thresholdValue; 


blobMeasurements=regionprops(BW,originalImage,'all')



% test if the bounding boxes are correctly located
subplot(2,1,1)
imshow(originalImage);
axis image; % Make sure image is not artificially stretched because of screen's aspect ratio.

hold on;
boundaries = bwboundaries(BW);
numberOfBoundaries = size(boundaries, 1);

for k = 1 : numberOfBoundaries
	thisBoundary = boundaries{k};
	plot(thisBoundary(:,2), thisBoundary(:,1), 'g', 'LineWidth', 1);
	
end
hold off;
 subplot(2,1,2)
 imshow(I)

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




