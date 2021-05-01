# Image-Histogram-Equalization
히스토그램 평활화와 YCbCr 색공간을 이용한 이미지 개선

YCbCr은 영상처리 분야에서 사용되는 색공간의 일종이다. Y는 luma(빛의 세기), Cb,Cr은 chroma(색의 차이) 성분이다.

YCbCr은 보통 영상의 압축에 많이 이용된다. 보통 사람의 눈은 luma 성분에 예민하고, chroma 성분에 상대적으로 덜 예민하다. 때문에 이러한 특징을 활용하여 Y성분에 많은 픽셀수를 할당하고, Cb, Cr성분은 낮은 픽셀 수를 할당함으로써 압축을 진행한다.


프로젝트에서는 이 Y성분에만 히스토그램 평활화(Histogram Equalization)를 진행해서, 이미지의 품질에 어떤 영향을 미치는지 확인하려고 한다.
