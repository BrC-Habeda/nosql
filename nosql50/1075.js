// Define data insertion
const data = {
project: [
    { project_id: 1, employee_id: 1 },
    { project_id: 1, employee_id: 2 },
    { project_id: 1, employee_id: 3 },
    { project_id: 2, employee_id: 1 },
    { project_id: 2, employee_id: 4 }
],
employee: [
    { employee_id: 1, name: 'Khaled', experience_years: 3 },
    { employee_id: 2, name: 'Ali', experience_years: 2 },
    { employee_id: 3, name: 'John', experience_years: 1 },
    { employee_id: 4, name: 'Doe', experience_years: 2 }
]
};

// Define aggregation pipeline
const pipeline = [
{
    $lookup: {
    from: "employee",
    localField: "employee_id",
    foreignField: "employee_id",
    as: "employee_info"
    }
},
{
    $unwind: "$employee_info"
},
{
    $group: {
    _id: "$project_id",
    average_experience_years: { $avg: "$employee_info.experience_years" }
    }
},
{
    $project: {
    _id: 0,
    project_id: "$_id",
    average_experience_years: { $round: ["$average_experience_years", 2] }
    }
}
];

// Define expected result
const expected_result = [
    { project_id: 1, average_experience_years: 2.0 },
    { project_id: 2, average_experience_years: 2.5 }
];

// Export data insertion, pipeline, and expected result
module.exports = { data, pipeline, expected_result };
