from app import app, db, Question

# Veritabanını oluştur
with app.app_context():
    db.create_all()

    # Yeni soruları ekle
    q1 = Question(
        question="Yapay Zeka (AI) nedir?", 
        option1="Bir tür bilgisayar donanımı", 
        option2="Düşünebilen ve öğrenebilen bir makine", 
        option3="Bir programlama dili", 
        correct_answer="Düşünebilen ve öğrenebilen bir makine"
    )
    
    q2 = Question(
        question="Aşağıdakilerden hangisi bilgisayar görüşü uygulamalarından biridir?", 
        option1="Konuşma tanıma", 
        option2="Görüntü sınıflandırma", 
        option3="Metin oluşturma", 
        correct_answer="Görüntü sınıflandırma"
    )
    
    q3 = Question(
        question="NLP nedir?", 
        option1="Sinirsel Dil İşleme", 
        option2="Doğal Dil İşleme", 
        option3="Yeni Seviye Programlama", 
        correct_answer="Doğal Dil İşleme"
    )
    
    q4 = Question(
        question="Python ile AI modelleri oluşturmak için yaygın olarak hangi kütüphane kullanılır?", 
        option1="Flask", 
        option2="TensorFlow", 
        option3="Django", 
        correct_answer="TensorFlow"
    )
    
    q5 = Question(
        question="Bir yapay zeka modelinin eğitilmesinin amacı nedir?", 
        option1="Veri toplamak", 
        option2="Tahmin veya karar vermek", 
        option3="Kod yazmak", 
        correct_answer="Tahmin veya karar vermek"
    )

    # Soruları veritabanına ekle
    db.session.add(q1)
    db.session.add(q2)
    db.session.add(q3)
    db.session.add(q4)
    db.session.add(q5)

    # Değişiklikleri kaydet
    db.session.commit()

    print("Veritabanı oluşturuldu ve sorular eklendi.")
