{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Laboratory_No_8(1).py",
      "provenance": [],
      "authorship_tag": "ABX9TyPtWvy8nxi70URhfK4aNrKa",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ECBelarmino/OOP-58001/blob/main/Laboratory_No_8(1).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Laboratory Activity 8 - Method 1**"
      ],
      "metadata": {
        "id": "FPuO_edDtTPO"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oLPqvYRitOV9",
        "outputId": "f62f14a5-61c3-469d-b142-b01ff15bd0c4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first number:43\n",
            "Enter the second number:38\n",
            "Enter the third number:69\n",
            "The largest number among the three is: 69\n"
          ]
        }
      ],
      "source": [
        "#TUI Form\n",
        "def main():\n",
        "    # Find the largest number among three numbers\n",
        "    L = []\n",
        "    num1 = eval(input(\"Enter the first number:\"))\n",
        "    L.append(num1)\n",
        "    num2 = eval(input(\"Enter the second number:\"))\n",
        "    L.append(num2)\n",
        "    num3 = eval(input(\"Enter the third number:\"))\n",
        "    L.append(num3)\n",
        "    print(\"The largest number among the three is:\",str(max(L)))\n",
        "\n",
        "main()\n"
      ]
    }
  ]
}