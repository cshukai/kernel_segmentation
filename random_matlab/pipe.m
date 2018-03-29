%%%%%%%%%%%%%%%%%%%%%%%approach 1 : directly background removal from RGB%%%%%%%%%%%%%

I=imread('DSC_0785.tiff')
red_binary = I(:,:,1)  >110 | I(:,:,1)<50 ;
green_binary = I(:,:,2)  <80 | I(:,:,2)  >140;
blue_binary= I(:,:,3)  <90 |  I(:,:,3)  >160;
final_mask = red_binary & green_binary & blue_binary;

% manually move the color meter away

%%%%%%%%%%%%%%%%%approach 2: color thresholding for regionprop###################
img=imread('DSC_0628.NEF')

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


%%%%%%%%%%%%%%%%%%%%%%%%%%approach 3: background-substraction-based approach%%%%%%%%%%%
img=imread('DSC_0668.NEF')
fore = double(img)/255;
back = double(imread('DSC_0675.NEF'))/255;
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


%%%%%%%%%%%%%approach 4: ostu ##############
imagefiles = dir('*.NEF');      
nfiles = length(imagefiles);

for ii=1:nfiles
   currentfilename = imagefiles(ii).name;
   currentimage = imread(currentfilename);
 
   %ostu
   %https://www.mathworks.com/help/images/examples/correcting-nonuniform-illumination.html
   currentimage=imadjust(rgb2gray(currentimage))
   bw = imbinarize(currentimage);
   bw = bwareaopen(bw, 50); % not bigger than 50 pixel
   cc = bwconncomp(bw, 4)
   labeled = labelmatrix(cc);
   RGB_label = label2rgb(labeled, @spring, 'c', 'shuffle');
   out=strcat(currentfilename,'ostu.tiff')
   imwrite(RGB_label,out)
   
end


%%%%%%%%%%%%%approach 5: k mean clustering ##############
%https://www.mathworks.com/help/images/examples/color-based-segmentation-using-k-means-clustering.html?prodcode=IP&language=en
imagefiles = dir('*.NEF');      
nfiles = length(imagefiles);

for ii=1:nfiles
   currentfilename = imagefiles(ii).name;
   he = imread(currentfilename);
  
   cform = makecform('srgb2lab');
   lab_he = applycform(he,cform);
  
   ab = double(lab_he(:,:,2:3));
	nrows = size(ab,1);
	ncols = size(ab,2);
	ab = reshape(ab,nrows*ncols,2);

	nColors = 30;
	% repeat the clustering 3 times to avoid local minima
	[cluster_idx, cluster_center] = kmeans(ab,nColors,'distance','sqEuclidean', 'Replicates',3,'MaxIter',1000);
	pixel_labels = reshape(cluster_idx,nrows,ncols);
	segmented_images = cell(1,3);
	rgb_label = repmat(pixel_labels,[1 1 3]);
	for k = 1:nColors
    	color = he;
    	color(rgb_label ~= k) = 0;
    	segmented_images{k} = color;
    	out=strcat(currentfilename,'cluster_',num2str(k),'.tiff')
    	imwrite(segmented_images{k},out)
	end
   
end

%%%%approach 6: watershed %%%%%%%%
imagefiles = dir('*.NEF');      
nfiles = length(imagefiles);

for ii=1:nfiles
   currentfilename = imagefiles(ii).name;
   rgb = imread(currentfilename);
   I = rgb2gray(rgb);
   
   hy = fspecial('sobel');
hx = hy';
Iy = imfilter(double(I), hy, 'replicate');
Ix = imfilter(double(I), hx, 'replicate');
gradmag = sqrt(Ix.^2 + Iy.^2);
   
   L = watershed(gradmag);
Lrgb = label2rgb(L);
se = strel('disk', 20);
Io = imopen(I, se);
Ie = imerode(I, se);
Iobr = imreconstruct(Ie, I);
Ioc = imclose(Io, se);
Iobrd = imdilate(Iobr, se);
Iobrcbr = imreconstruct(imcomplement(Iobrd), imcomplement(Iobr));
Iobrcbr = imcomplement(Iobrcbr);
fgm = imregionalmax(Iobrcbr);
%todo
end



%%%%%%%%%%%%%%%convert to different color space for shadow removal and apply edge detection
I = imread('DSC_0785.tiff');  % your original image
%I=imcrop(I)
I=rgb2lab(I)
blue_binary=  I(:,:,3)  >-15;
imwrite(blue_binary,'shadow_removed_lab.tiff')


