# FooBao_textOCR1

생성자: 양재원
생성 일시: 2023년 12월 6일 오전 12:07
태그: 제품

메뉴판 OCR은 다음과 같은 순서로 진행됩니다.

1. 메뉴판 이미지 input
2. 학습된 모델로 메뉴판 속 메뉴명만 detection한 후, 메뉴명 bounding box 이외의 부분은 Blurring
3. Pororo OCR 모델을 통해 blur된 이미지 속 메뉴명만을 read
4. 위의 OCR을 통해 생성된 menu_ocr.txt를 CLIP_text_similarity.ipynb 에서 유사도 결과 확인
   (만약 해당 ipynb가 실행이 안될 경우 FooBao_imageSimilarity reposit에서 생성한 가상환경에서 실행하시길 부탁드립니다)

사용한 모델

- YOLOv5
    - 메뉴판 속 메뉴명만 detection 하도록 학습 진행
- Pororo from Kakaobrain
    - 한국어 ocr 모델로, 이미지 속 메뉴명을 텍스트로 추출
