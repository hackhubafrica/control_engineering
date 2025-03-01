clear all; close all; clc

addpath('../apm')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Configuration
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% number of terms
ny = 3; % output coefficients
nu = 3; % input coefficients
% number of inputs
ni = 2;
% number of outputs
no = 2;
% load data and parse into columns
load data_no_headers.csv
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% generate state space model
sysd = apm_id(data_no_headers,ni,nu,ny);
