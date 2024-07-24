// Gmsh project created on Mon Mar 11 19:07:32 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {100, 0, 0, 1.0};
//+
Point(3) = {100, 100, 0, 1.0};
//+
Point(4) = {0, 100, 0, 1.0};
//+
Point(5) = {25, 100, 0, 1.0};
//+
Point(6) = {26, 100, 0, 1.0};
//+
Point(7) = {74, 100, 0, 1.0};
//+
Point(8) = {75, 100, 0, 1.0};
//+
Point(9) = {75, 25, 0, 1.0};
//+
Point(10) = {74, 26, 0, 1.0};
//+
Point(11) = {25, 25, 0, 1.0};
//+
Point(12) = {26, 26, 0, 1.0};
//+
Point(13) = {25, 99, 0, 1.0};
//+
Point(14) = {26, 99, 0, 1.0};
//+
Point(15) = {75, 99, 0, 1.0};
//+
Point(16) = {74, 99, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 15};
//+
Line(4) = {15, 9};
//+
Line(5) = {9, 11};
//+
Line(6) = {11, 13};
//+
Line(7) = {13, 4};
//+
Line(8) = {4, 1};
//+
Curve Loop(1) = {8, 1, 2, 3, 4, 5, 6, 7};
//+
Surface(1) = {1};
//+
Line(9) = {14, 12};
//+
Line(10) = {12, 10};
//+
Line(11) = {10, 16};
//+
Line(12) = {16, 14};
//+
Line(13) = {15, 8};
//+
Line(14) = {8, 7};
//+
Line(15) = {7, 16};
//+
Line(16) = {14, 6};
//+
Line(17) = {6, 5};
//+
Line(18) = {5, 13};
//+
Curve Loop(3) = {10, 11, 12, 9};
//+
Surface(2) = {3};
//+
Curve Loop(5) = {5, 6, -18, -17, -16, 9, 10, 11, -15, -14, -13, 4};
//+
Surface(3) = {5};
//+
Physical Surface("Boden", 19) = {1, 2};
//+
Physical Surface("Rohr", 20) = {3};
//+
Physical Curve("Rohr", 21) = {5, 4, 13, 15, 11, 10, 9, 16, 18, 6};
//+
Physical Curve("BodenTemp", 22) = {1};
//+
Physical Curve("RohrOutr", 23) = {14};
//+
Physical Curve("RohrInl", 24) = {17};

MeshSize{:} = 2;

Mesh 2;


save "prj_ground_sketch.msh";
