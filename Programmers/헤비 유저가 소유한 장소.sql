-- �ڵ带 �Է��ϼ���
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (  SELECT HOST_ID
                    FROM PLACES
                    GROUP BY HOST_ID
                    HAVING count(*) > 1) 