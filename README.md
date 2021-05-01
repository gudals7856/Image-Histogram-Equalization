# Histogram Equalization과 YCbCr 색공간을 이용한 이미지 개선
---------------
## 프로젝트 설명
>YCbCr은 영상처리 분야에서 사용되는 색공간의 일종이다. Y는 luma(빛의 세기), Cb,Cr은 chroma(색의 차이) 성분이다.

>YCbCr은 보통 영상의 압축에 많이 이용된다. 보통 사람의 눈은 luma 성분에 예민하고, chroma 성분에 상대적으로 덜 예민하다. 때문에 이러한 특징을 활용하여 Y성분에 많은 픽셀수를 할당하고, Cb, Cr성분은 낮은 픽셀 수를 할당함으로써 압축을 진행한다.

>프로젝트에서는 이 Y성분에만 히스토그램 평활화(Histogram Equalization)를 진행해서, 이미지의 품질에 어떤 영향을 미치는지 확인하려고 한다.
-------------------


## 프로젝트 진행 과정
> 1. Input Image의 RGB성분을 분리해 in_B, in_G, in_R 로 정의한다.(cv2.split을 진행하면 BGR순으로 나옴)
> 2. rgb_to_ycbcr함수를 통해 ycbcr로 변환하고 in_Y, Cb, Cr 로 정의한다. (Cb와 Cr은 사용 X)
> 3. Y 채널에 히스토그램 평활화를 적용한다.
> 4. 히스토그램 평활화가 적용된 Y채널 값과  위 사진의 알고리즘을 이용해 Output Image의 RGB값을 구한다.
> 5. RGB값을 merge하여 하나의 이미지로 만든다.
--------------------


## 실행 결과
적용 전 이미지(Input Image)

![image](https://user-images.githubusercontent.com/76733288/116774271-77ffc800-aa96-11eb-8c8a-d8828265de32.png)

적용 후 이미지(Output Image)

![image](https://user-images.githubusercontent.com/76733288/116774286-91087900-aa96-11eb-8808-032881088f32.png)

Input Image에서는 픽셀값이 낮은 부분으로 대부분의 픽셀이 모여있다. Histogram Equalization을 적용해 나온 Output Image에서는 어두운 부분에 많이 몰려있던 픽셀들이 넓게 퍼졌기 때문에 비교적 밝아진 결과물을 확인할 수 있다.
