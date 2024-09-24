"""


-- hw.24.09.2024

-- 1.a:

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON DELETE CASCADE
);
-- ON DELETE CASCADE:
-- הוא מנגנון שמבצע מחיקה אוטומטית של רשומות בטבלה המקושרת
--  זאת אומרת שאם נמחק רישום בטבלה (departments), אז כל הרישומים הקשורים בטבלה (employees) נמחקים אוטומטית
-- זה מסייע בשמירה על ניקוי אוטומטי של הנתונים

-- 1.b:

-- במקרה של מפתח זר רגיל (FK), אם רשומה נמחקת מהטבלה הראשית (כמו departments),
-- תתרחש שגיאה אם יש עדיין רשומות בטבלה המשנית (כמו employees) התלויות בה.
-- משמעות הדבר היא שאינך יכול למחוק מחלקה אם ישנם עובדים המקושרים אליה.

-- 1.c:

-- מגביר את הבטיחות:
-- אפשר לטעון ששימוש ב-CASCADE DELETE
-- יכול להפחית את הסיכון לנתונים יתומים בטבלה המשנית,
-- שכן המערכת דואגת למחוק את כל הרשומות הקשורות.

-- מקטין את הבטיחות:
-- מצד שני, זה עלול להפחית את הבטיחות בכך שמשתמשים לא תמיד מודעים למחיקות שיתרחשו,
-- מה שעלול להוביל לאובדן לא מכוון של נתונים חשובים.
-- חשוב להיזהר בשימוש ב-CASCADE DELETE,
-- שכן מחיקות לא מכוונות עלולות לגרום לאובדן נתונים משמעותי.

-- 2.

CREATE TABLE random_numbers (
    id SERIAL PRIMARY KEY,
    random_value DECIMAL
);

INSERT INTO random_numbers (random_value)
SELECT ROUND((RANDOM() * 100)::numeric, 2)
FROM generate_series(1, 10);

SELECT * FROM random_numbers;

SELECT * FROM random_numbers
ORDER BY RANDOM()
LIMIT 3;

UPDATE random_numbers
SET random_value = ROUND((RANDOM() * 100)::numeric, 2)
WHERE id = 1;


SELECT * FROM random_numbers;

-- 2.a:

-- הסבר מה עושה הקוד?
-- הקוד יוצר טבלה, מוסיף 10 ערכים אקראיים, מאחזר ומציג את כל הרשומות, בוחר באקראי 3 רשומות,
-- מעדכן רשומה ספציפית אחת בערך אקראי חדש, ומחזיר את כל הרשומות שוב כדי לשקף את העדכון.

-- 2.b:

-- מה עושה ::numeric ?

-- ב-SQL, סוג הנתונים NUMERIC (או DECIMAL) משמש לאחסון ערכים מספריים מדויקים עם דיוק וקנה מידה מוגדרים.
-- להלן פירוט המאפיינים שלו:
--
-- דיוק: זה מתייחס למספר הכולל של הספרות שניתן לאחסן, הן משמאל והן מימין לנקודה העשרונית.
-- לדוגמה, סוג NUMERIC(5, 2) יכול לאחסן מספרים עד 999.99.
--
-- קנה מידה: זה מציין את מספר הספרות שניתן לאחסן מימין לנקודה העשרונית.
-- בדוגמה למעלה, הסולם הוא 2, כלומר 2 ספרות יכולות להיות אחרי העשרוני.
--
-- ייצוג מדויק: בניגוד לסוגי נקודה צפה (כמו FLOAT או REAL),
-- שיכולים להציג שגיאות עיגול בשל הייצוג הבינארי שלהם, NUMERIC מספק ייצוג מדויק.
-- זה חשוב במיוחד עבור חישובים פיננסיים שבהם הדיוק הוא קריטי.
--
-- טווח: טווח הערכים שניתן לאחסן בסוג NUMERIC תלוי בדיוק ובקנה מידה שהוגדרו.

-- 2.c:

-- RANDOM()
-- פונקציה: RANDOM() היא פונקציה מובנית ב-SQL (במיוחד ב-PostgreSQL)
-- שיוצרת מספר אקראי של נקודה צפה בין 0 (כולל) ל-1 (בלעדי).
-- שימוש: ניתן להשתמש בו בהקשרים שונים, כגון הפקת ערכים אקראיים,
-- בחירת רשומות אקראיות או הכנסת אקראיות בחישובים.

-- ROUND()
-- פונקציה: ROUND(numeric_value, decimal_places)
--היא פונקציה המעגלת ערך מספרי נתון למספר מוגדר של מקומות עשרוניים.

-- פרמטרים:
-- numeric_value: המספר שברצונך לעגל.
-- decimal_places: מספר המקומות העשרוניים שאליהם יש לעגל.
-- אם זה מושמט, ברירת המחדל של הפונקציה היא עיגול למספר השלם הקרוב ביותר.
-- שימוש: פונקציה זו שימושית לעיצוב מספרים,
-- כדי להבטיח שהם עומדים בדרישות דיוק ספציפיות (כמו ביישומים פיננסיים),
-- או פשוט להפוך את הפלט לקריאה יותר.

-- בקוד ה-SQL הזה:
--
-- RANDOM() יוצר עשרוני אקראי בין 0 ל-1.
-- הכפלה ב-100 סולמות שערכם בין 0 ל-100.
-- ROUND(..., 2) לאחר מכן מעגל את התוצאה לשני מקומות עשרוניים,
-- ומייצר ערך אקראי כמו 23.45 או 67.89 שניתן לאחסן בעמודה random_value.
-- יחד, הם יוצרים מספרים עשרוניים אקראיים המתאימים ליישומים שונים תוך הבטחת הצגת הערכים בצורה נקייה ומעוצבת.

-- 2.d:

-- GENERATE_SERIES:
-- היא פונקציה להחזרת סטים ב- PostgreSQL שיוצרת סדרה של מספרים או חותמות זמן.
-- היא משמשת לעתים קרובות ליצירת רצפים בשאילתות,
-- והיא יכולה להיות שימושית מאוד בתרחישים כמו הוספת שורות מרובות, ביצוע חישובים או יצירת נתוני בדיקה.



-- 3.

    CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    sale_amount DECIMAL(10, 2),
    sale_timestamp TIMESTAMP
);

-- Insert sample data with timestamps
INSERT INTO sales (product_name, sale_amount, sale_timestamp) VALUES
('Laptop', 1200.50, '2024-01-10 10:30:00'),
('Smartphone', 800.00, '2024-01-15 14:45:00'),
('Tablet', 450.75, '2024-02-05 09:00:00'),
('Monitor', 250.00, '2024-03-10 11:15:00'),
('Keyboard', 50.00, '2024-03-12 16:30:00');

SELECT * FROM sales
WHERE sale_timestamp >= '2024-03-01 00:00:00'
AND sale_timestamp < '2024-04-01 00:00:00';

SELECT * FROM sales
WHERE EXTRACT(DOW FROM sale_timestamp) IN (0, 6);

SELECT * FROM sales
WHERE sale_timestamp >= NOW() - INTERVAL '7 days';

SELECT * FROM sales
WHERE EXTRACT(HOUR FROM sale_timestamp) BETWEEN 9 AND 17;

SELECT DATE(sale_timestamp) AS sale_date, COUNT(*) AS total_sales
FROM sales
GROUP BY DATE(sale_timestamp)
ORDER BY sale_date;

SELECT DATE(sale_timestamp) AS sale_date, COUNT(*) AS total_sales
FROM sales
GROUP BY DATE(sale_timestamp)
ORDER BY sale_date;

SELECT * FROM sales
WHERE EXTRACT(HOUR FROM sale_timestamp) < 12;

SELECT product_name, MIN(sale_timestamp) AS first_sale
FROM sales
GROUP BY product_name;

SELECT product_name, MAX(sale_timestamp) AS last_sale
FROM sales
GROUP BY product_name;

SELECT DATE(sale_timestamp) AS sale_date, SUM(sale_amount) AS total_sales
FROM sales
WHERE EXTRACT(HOUR FROM sale_timestamp) BETWEEN 12 AND 14
GROUP BY DATE(sale_timestamp);

-- 3.a:
-- הסבר מה כל שאילתא עושה?

-- בחינת מכירות בתקופה מסוימת: הצגת מכירות שנעשו בין 1 במרץ ל-31 במרץ 2024.
--
-- מכירות בימי סוף שבוע: הצגת מכירות שבוצעו בימים ראשון ושבת.
--
-- מכירות בשבוע האחרון: הצגת מכירות שבוצעו בשבעת הימים האחרונים.
--
-- מכירות בשעות העבודה: הצגת מכירות שבוצעו בין השעות 9 ל-17.
--
-- ספירת מכירות לפי תאריך: הצגת מספר המכירות לכל תאריך.
--
-- ספירת מכירות לפי תאריך: הצגת מספר המכירות לכל תאריך (חזרה על השאילתה הקודמת).
--
-- מכירות לפני הצהריים: הצגת מכירות שבוצעו לפני השעה 12:00.
--
-- מכירה ראשונה לכל מוצר: הצגת תאריך המכירה הראשון של כל מוצר.
--
-- מכירה אחרונה לכל מוצר: הצגת תאריך המכירה האחרון של כל מוצר.
--
-- סכום מכירות בשעות מסוימות: הצגת סכום המכירות שנעשו בין השעות 12 ל-14 לפי תאריך.
"""