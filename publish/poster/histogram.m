I=imread('DSC_0785.NEFleft.tiff')
figure
imhist(I(:,:,3))
title('Blue Channel of Sample Background Images')
xlabel('Pixel  Values') % x-axis label
ylabel('Frequency') % y-axis label

I=imread('DSC_0785.tiffkernel.tiff')
%subplot(3:1,1)
figure
imhist(I(:,:,3))
title('Blue Channel of Sample Kernel Image')
xlabel('Pixel  Values') % x-axis label
ylabel('Frequency') % y-axis label
%subplot(3:1,2)
figure
imhist(I(:,:,2))
title('Green Channel of Sample Kernel Images')
xlabel('Pixel  Values') % x-axis label
ylabel('Frequency') % y-axis label

%subplot(3:1,3)
figure
imhist(I(:,:,1))
title('Red Channel of Sample Kernel Image')
xlabel('Pixel  Values') % x-axis label
ylabel('Frequency') % y-axis label