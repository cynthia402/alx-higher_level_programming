#!/usr/bin/python3
""" define function multiplies matrix"""
dot = __import__("numpy").dot


def lazy_matrix_mul(m_a, m_b):
    """ represent fuction """
    return dot(m_a, m_b)
