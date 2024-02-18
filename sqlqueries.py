consecutive_days_query ="""WITH ProjectActivityRanked AS (
    SELECT 
        ProjectID,
        Date,
        LAG(Date) OVER (PARTITION BY ProjectID ORDER BY Date) AS PrevDate,
        CASE 
            WHEN LAG(Date) OVER (PARTITION BY ProjectID ORDER BY Date) = Date - INTERVAL '1 day' THEN 0 
            ELSE 1 
        END AS IsNewGroup
    FROM 
        ProjectActivity
)

SELECT
    Date,
    ProjectID,
    SUM(IsNewGroup) OVER (PARTITION BY ProjectID ORDER BY Date) AS DaysInRow
FROM 
    ProjectActivityRanked
ORDER BY
    Date, ProjectID;
"""

abondaned_seven_query = """WITH ProjectUpdates AS (
    SELECT 
        Date,
        ProjectID,
        LAG(Date) OVER (PARTITION BY ProjectID ORDER BY Date) AS PrevDate
    FROM 
        ProjectActivity
),
ProjectAbandoned AS (
    SELECT 
        Date,
        ProjectID
    FROM 
        ProjectUpdates
    WHERE 
        DATEDIFF(day, PrevDate, Date) >= 7 OR PrevDate IS NULL
),
ProjectsModified AS (
    SELECT 
        Date,
        COUNT(DISTINCT ProjectID) AS CountProjectsModified
    FROM 
        ProjectActivity
    GROUP BY 
        Date
),
AbandonedCount AS (
    SELECT 
        pa.Date,
        COUNT(DISTINCT pa.ProjectID) AS CountAbandonedProjects
    FROM 
        ProjectAbandoned pa
    JOIN 
        ProjectActivity pa2 ON pa.ProjectID = pa2.ProjectID
    AND 
        DATEDIFF(day, pa.Date, pa2.Date) > 7
    GROUP BY 
        pa.Date
)
SELECT 
    pm.Date,
    COALESCE(ac.CountAbandonedProjects, 0) * 100.0 / pm.CountProjectsModified AS Abandoned_7
FROM 
    ProjectsModified pm
LEFT JOIN 
    AbandonedCount ac ON pm.Date = ac.Date
ORDER BY 
    pm.Date;
"""

retention_seven_query = """WITH ProjectCreation AS (
    SELECT 
        ProjectID,
        MIN(Date) AS CreationDate
    FROM 
        ProjectActivity
    GROUP BY 
        ProjectID
),
ProjectsCreated7DaysAgo AS (
    SELECT 
        ProjectID
    FROM 
        ProjectCreation
    WHERE 
        DATEADD(day, 7, CreationDate) = (SELECT MAX(Date) FROM ProjectActivity)
),
ProjectsUpdatedToday AS (
    SELECT 
        ProjectID
    FROM 
        ProjectActivity
    WHERE 
        Date = (SELECT MAX(Date) FROM ProjectActivity)
),
RetentionCount AS (
    SELECT 
        pa.Date,
        COUNT(DISTINCT CASE WHEN pc.ProjectID IS NOT NULL THEN pc.ProjectID END) AS RetainedProjects
    FROM 
        ProjectActivity pa
    LEFT JOIN 
        ProjectCreation pc ON pa.ProjectID = pc.ProjectID
    LEFT JOIN 
        ProjectsCreated7DaysAgo pcd ON pc.CreationDate = pcd.CreationDate
    WHERE 
        pcd.ProjectID IS NOT NULL
    AND 
        pa.ProjectID IN (SELECT ProjectID FROM ProjectsUpdatedToday)
    GROUP BY 
        pa.Date
)
SELECT 
    pa.Date,
    COALESCE(rc.RetainedProjects, 0) * 100.0 / COUNT(DISTINCT pc.ProjectID) AS Retention_7
FROM 
    ProjectActivity pa
JOIN 
    ProjectCreation pc ON pa.ProjectID = pc.ProjectID
LEFT JOIN 
    RetentionCount rc ON pa.Date = rc.Date
GROUP BY 
    pa.Date
ORDER BY 
    pa.Date;
"""