img=imread('DSC_0601.NEF')
I = imcrop(img)
originalImage=rgb2gray(I)
thresholdValue = 30; % 30 too little , 50 too large
binaryImage = originalImage > thresholdValue; 
blobMeasurements=regionprops(binaryImage,originalImage,'all')
allBlobIntensities = [blobMeasurements.MeanIntensity];
allBlobAreas = [blobMeasurements.Area];
% Get a list of the blobs that meet our criteria and we need to keep.
% These will be logical indices - lists of true or false depending on whether the feature meets the criteria or not.
% for example [1, 0, 0, 1, 1, 0, 1, .....].  Elements 1, 4, 5, 7, ... are true, others are false.
allowableIntensityIndexes = (allBlobIntensities > 150) & (allBlobIntensities < 220);
allowableAreaIndexes = allBlobAreas < 2000; % Take the small objects.
% Now let's get actual indexes, rather than logical indexes, of the  features that meet the criteria.
% for example [1, 4, 5, 7, .....] to continue using the example from above.
allAreas = [blobMeasurements.Area];
allPerims = [blobMeasurements.Perimeter];
circularities = allPerims .^ 2 ./ (4*pi*allAreas);
%keeperIndexes = find(allowableIntensityIndexes & allowableAreaIndexes);
keeperIndexes = find(circularities < 2 & allBlobAreas > 20);  

keeperBlobsImage = ismember(binaryImage, keeperIndexes);
