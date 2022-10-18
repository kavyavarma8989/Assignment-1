{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kavyavarma8989/Assignment-1/blob/main/Assignment_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f3e5d93c",
      "metadata": {
        "id": "f3e5d93c"
      },
      "source": [
        "1. Numpy:"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "18605fa9",
      "metadata": {
        "id": "18605fa9"
      },
      "source": [
        "Using NumPy create random vector of size 15 having only Integers in the range 1-20.\n",
        "1. Reshape the array to 3 by 5\n",
        "2. Print array shape.\n",
        "3. Replace the max in each row by 0"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "id": "f16ebb8e",
      "metadata": {
        "scrolled": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f16ebb8e",
        "outputId": "4c1daa51-80d2-452a-e363-d1672f2ede53"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Generated array:\n",
            "[13 12 18 16 12  9 11 11  5 16  7 11  8 11  5]\n"
          ]
        }
      ],
      "source": [
        "#Using numpy we created an array with 15 random elements\n",
        "\n",
        "import numpy as np\n",
        "x = np.random.randint(1,20,15)\n",
        "print(\"Generated array:\")\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "id": "17dcf573",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "17dcf573",
        "outputId": "c5f00ba0-26b9-481b-8baa-df133816f5fc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reshaped array: \n",
            " [[13 12 18 16 12]\n",
            " [ 9 11 11  5 16]\n",
            " [ 7 11  8 11  5]]\n",
            "Shape of the array  (3, 5)\n"
          ]
        }
      ],
      "source": [
        "#Reshape the array to 3 by 5\n",
        "#Print array shape.\n",
        "\n",
        "\n",
        "y=np.reshape(x, [3, 5])\n",
        "print(\"Reshaped array: \\n\",y)\n",
        "print(\"Shape of the array \",y.shape)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "id": "2616c421",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2616c421",
        "outputId": "32756f1d-ee29-4b6c-eb1f-f6e5cce5e73d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[13 12  0 16 12]\n",
            " [ 9 11 11  5  0]\n",
            " [ 7  0  8  0  5]]\n"
          ]
        }
      ],
      "source": [
        "#Replace the max in each row by 0\n",
        "\n",
        "for i in y:\n",
        "    i[i == max(i)] = 0\n",
        "print(y)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "8f237f67",
      "metadata": {
        "id": "8f237f67"
      },
      "source": [
        "2. Pandas"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "00e4538e",
      "metadata": {
        "id": "00e4538e"
      },
      "source": [
        "1. Read the provided CSV file ‘data.csv’.\n",
        "https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing\n",
        "2. Show the basic statistical description about the data.\n",
        "3. Check if the data has null values.\n",
        "a. Replace the null values with the mean\n",
        "4. Select at least two columns and aggregate the data using: min, max, count, mean.\n",
        "5. Filter the dataframe to select the rows with calories values between 500 and 1000.\n",
        "6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.\n",
        "7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.\n",
        "8. Delete the “Maxpulse” column from the main df dataframe\n",
        "9. Convert the datatype of Calories column to int datatype.\n",
        "10. Using pandas create a scatter plot for the two columns (Duration and Calories).\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "96301e85",
      "metadata": {
        "id": "96301e85"
      },
      "source": [
        "1"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "id": "caa28886",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "caa28886",
        "outputId": "b5a7bdd2-5212-4c7c-e46e-259cbcf343c1"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Duration  Pulse  Maxpulse  Calories\n",
              "0        60    110       130     409.1\n",
              "1        60    117       145     479.0\n",
              "2        60    103       135     340.0\n",
              "3        45    109       175     282.4\n",
              "4        45    117       148     406.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ba001e11-7e87-4b8c-8124-9566fd46a3ee\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Duration</th>\n",
              "      <th>Pulse</th>\n",
              "      <th>Maxpulse</th>\n",
              "      <th>Calories</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>60</td>\n",
              "      <td>110</td>\n",
              "      <td>130</td>\n",
              "      <td>409.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>60</td>\n",
              "      <td>117</td>\n",
              "      <td>145</td>\n",
              "      <td>479.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>60</td>\n",
              "      <td>103</td>\n",
              "      <td>135</td>\n",
              "      <td>340.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>45</td>\n",
              "      <td>109</td>\n",
              "      <td>175</td>\n",
              "      <td>282.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>45</td>\n",
              "      <td>117</td>\n",
              "      <td>148</td>\n",
              "      <td>406.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ba001e11-7e87-4b8c-8124-9566fd46a3ee')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ba001e11-7e87-4b8c-8124-9566fd46a3ee button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ba001e11-7e87-4b8c-8124-9566fd46a3ee');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "data = pd.read_csv(\"data.csv\")\n",
        "data.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "a5e4f103",
      "metadata": {
        "id": "a5e4f103"
      },
      "source": [
        "2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "id": "0c46f843",
      "metadata": {
        "scrolled": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "0c46f843",
        "outputId": "eb73152f-fcf3-4156-8c7f-95728d027ca7"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         Duration       Pulse    Maxpulse     Calories\n",
              "count  169.000000  169.000000  169.000000   164.000000\n",
              "mean    63.846154  107.461538  134.047337   375.790244\n",
              "std     42.299949   14.510259   16.450434   266.379919\n",
              "min     15.000000   80.000000  100.000000    50.300000\n",
              "25%     45.000000  100.000000  124.000000   250.925000\n",
              "50%     60.000000  105.000000  131.000000   318.600000\n",
              "75%     60.000000  111.000000  141.000000   387.600000\n",
              "max    300.000000  159.000000  184.000000  1860.400000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-6635247b-be5c-46ed-8884-5e4da879ce0f\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Duration</th>\n",
              "      <th>Pulse</th>\n",
              "      <th>Maxpulse</th>\n",
              "      <th>Calories</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>169.000000</td>\n",
              "      <td>169.000000</td>\n",
              "      <td>169.000000</td>\n",
              "      <td>164.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>63.846154</td>\n",
              "      <td>107.461538</td>\n",
              "      <td>134.047337</td>\n",
              "      <td>375.790244</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>42.299949</td>\n",
              "      <td>14.510259</td>\n",
              "      <td>16.450434</td>\n",
              "      <td>266.379919</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>15.000000</td>\n",
              "      <td>80.000000</td>\n",
              "      <td>100.000000</td>\n",
              "      <td>50.300000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>45.000000</td>\n",
              "      <td>100.000000</td>\n",
              "      <td>124.000000</td>\n",
              "      <td>250.925000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>60.000000</td>\n",
              "      <td>105.000000</td>\n",
              "      <td>131.000000</td>\n",
              "      <td>318.600000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>60.000000</td>\n",
              "      <td>111.000000</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>387.600000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>300.000000</td>\n",
              "      <td>159.000000</td>\n",
              "      <td>184.000000</td>\n",
              "      <td>1860.400000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6635247b-be5c-46ed-8884-5e4da879ce0f')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-6635247b-be5c-46ed-8884-5e4da879ce0f button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-6635247b-be5c-46ed-8884-5e4da879ce0f');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "data.describe()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "6b9cec31",
      "metadata": {
        "id": "6b9cec31"
      },
      "source": [
        "3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "id": "b6ff0559",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b6ff0559",
        "outputId": "cc38b01a-82bf-4201-b9df-200207491232"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Duration    False\n",
              "Pulse       False\n",
              "Maxpulse    False\n",
              "Calories     True\n",
              "dtype: bool"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "data.isnull().any()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "id": "71da4222",
      "metadata": {
        "scrolled": false,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "71da4222",
        "outputId": "91ca3a49-6728-4062-bb97-74c0f407fbea"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Duration    False\n",
              "Pulse       False\n",
              "Maxpulse    False\n",
              "Calories    False\n",
              "dtype: bool"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ],
      "source": [
        "data.fillna(data.mean(), inplace=True)\n",
        "data.isnull().any()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "062dd34e",
      "metadata": {
        "id": "062dd34e"
      },
      "source": [
        "4"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "id": "b446fbd3",
      "metadata": {
        "scrolled": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        },
        "id": "b446fbd3",
        "outputId": "06c49e6e-5f54-4504-a10d-17b5a2568b11"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         Maxpulse     Calories\n",
              "min    100.000000    50.300000\n",
              "max    184.000000  1860.400000\n",
              "count  169.000000   169.000000\n",
              "mean   134.047337   375.790244"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-340b6ebe-3f21-4173-874f-e5e55eabe160\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Maxpulse</th>\n",
              "      <th>Calories</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>100.000000</td>\n",
              "      <td>50.300000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>184.000000</td>\n",
              "      <td>1860.400000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>169.000000</td>\n",
              "      <td>169.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>134.047337</td>\n",
              "      <td>375.790244</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-340b6ebe-3f21-4173-874f-e5e55eabe160')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-340b6ebe-3f21-4173-874f-e5e55eabe160 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-340b6ebe-3f21-4173-874f-e5e55eabe160');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "data.agg({'Maxpulse':['min','max','count','mean'],'Calories':['min','max','count','mean']})"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "7972dddb",
      "metadata": {
        "id": "7972dddb"
      },
      "source": [
        "5"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "id": "2a7615d4",
      "metadata": {
        "scrolled": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 488
        },
        "id": "2a7615d4",
        "outputId": "302e7397-5f23-453d-a052-a42bbcb81a89"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     Duration  Pulse  Maxpulse  Calories\n",
              "51         80    123       146     643.1\n",
              "62        160    109       135     853.0\n",
              "65        180     90       130     800.4\n",
              "66        150    105       135     873.4\n",
              "67        150    107       130     816.0\n",
              "72         90    100       127     700.0\n",
              "73        150     97       127     953.2\n",
              "75         90     98       125     563.2\n",
              "78        120    100       130     500.4\n",
              "90        180    101       127     600.1\n",
              "99         90     93       124     604.1\n",
              "103        90     90       100     500.4\n",
              "106       180     90       120     800.3\n",
              "108        90     90       120     500.3"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a888f23d-377f-453c-92b9-3ba2b3352009\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Duration</th>\n",
              "      <th>Pulse</th>\n",
              "      <th>Maxpulse</th>\n",
              "      <th>Calories</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>51</th>\n",
              "      <td>80</td>\n",
              "      <td>123</td>\n",
              "      <td>146</td>\n",
              "      <td>643.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>62</th>\n",
              "      <td>160</td>\n",
              "      <td>109</td>\n",
              "      <td>135</td>\n",
              "      <td>853.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>65</th>\n",
              "      <td>180</td>\n",
              "      <td>90</td>\n",
              "      <td>130</td>\n",
              "      <td>800.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>66</th>\n",
              "      <td>150</td>\n",
              "      <td>105</td>\n",
              "      <td>135</td>\n",
              "      <td>873.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>67</th>\n",
              "      <td>150</td>\n",
              "      <td>107</td>\n",
              "      <td>130</td>\n",
              "      <td>816.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>72</th>\n",
              "      <td>90</td>\n",
              "      <td>100</td>\n",
              "      <td>127</td>\n",
              "      <td>700.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>73</th>\n",
              "      <td>150</td>\n",
              "      <td>97</td>\n",
              "      <td>127</td>\n",
              "      <td>953.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75</th>\n",
              "      <td>90</td>\n",
              "      <td>98</td>\n",
              "      <td>125</td>\n",
              "      <td>563.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>78</th>\n",
              "      <td>120</td>\n",
              "      <td>100</td>\n",
              "      <td>130</td>\n",
              "      <td>500.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>90</th>\n",
              "      <td>180</td>\n",
              "      <td>101</td>\n",
              "      <td>127</td>\n",
              "      <td>600.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>99</th>\n",
              "      <td>90</td>\n",
              "      <td>93</td>\n",
              "      <td>124</td>\n",
              "      <td>604.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>103</th>\n",
              "      <td>90</td>\n",
              "      <td>90</td>\n",
              "      <td>100</td>\n",
              "      <td>500.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>106</th>\n",
              "      <td>180</td>\n",
              "      <td>90</td>\n",
              "      <td>120</td>\n",
              "      <td>800.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>108</th>\n",
              "      <td>90</td>\n",
              "      <td>90</td>\n",
              "      <td>120</td>\n",
              "      <td>500.3</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a888f23d-377f-453c-92b9-3ba2b3352009')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a888f23d-377f-453c-92b9-3ba2b3352009 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a888f23d-377f-453c-92b9-3ba2b3352009');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ],
      "source": [
        "data.loc[(data['Calories']>500)&(data['Calories']<1000)]"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "43ef5d65",
      "metadata": {
        "id": "43ef5d65"
      },
      "source": [
        "6"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "id": "887aacde",
      "metadata": {
        "scrolled": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "887aacde",
        "outputId": "ded550cb-b50b-47e8-a2ef-eec7b41a2363"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     Duration  Pulse  Maxpulse  Calories\n",
              "65        180     90       130     800.4\n",
              "70        150     97       129    1115.0\n",
              "73        150     97       127     953.2\n",
              "75         90     98       125     563.2\n",
              "99         90     93       124     604.1\n",
              "103        90     90       100     500.4\n",
              "106       180     90       120     800.3\n",
              "108        90     90       120     500.3"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-39677f5b-734b-4d5e-949f-647be26e2f79\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Duration</th>\n",
              "      <th>Pulse</th>\n",
              "      <th>Maxpulse</th>\n",
              "      <th>Calories</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>65</th>\n",
              "      <td>180</td>\n",
              "      <td>90</td>\n",
              "      <td>130</td>\n",
              "      <td>800.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>70</th>\n",
              "      <td>150</td>\n",
              "      <td>97</td>\n",
              "      <td>129</td>\n",
              "      <td>1115.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>73</th>\n",
              "      <td>150</td>\n",
              "      <td>97</td>\n",
              "      <td>127</td>\n",
              "      <td>953.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75</th>\n",
              "      <td>90</td>\n",
              "      <td>98</td>\n",
              "      <td>125</td>\n",
              "      <td>563.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>99</th>\n",
              "      <td>90</td>\n",
              "      <td>93</td>\n",
              "      <td>124</td>\n",
              "      <td>604.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>103</th>\n",
              "      <td>90</td>\n",
              "      <td>90</td>\n",
              "      <td>100</td>\n",
              "      <td>500.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>106</th>\n",
              "      <td>180</td>\n",
              "      <td>90</td>\n",
              "      <td>120</td>\n",
              "      <td>800.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>108</th>\n",
              "      <td>90</td>\n",
              "      <td>90</td>\n",
              "      <td>120</td>\n",
              "      <td>500.3</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-39677f5b-734b-4d5e-949f-647be26e2f79')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-39677f5b-734b-4d5e-949f-647be26e2f79 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-39677f5b-734b-4d5e-949f-647be26e2f79');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ],
      "source": [
        "data.loc[(data['Calories']>500)&(data['Pulse']<100)]"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "8d2670e0",
      "metadata": {
        "id": "8d2670e0"
      },
      "source": [
        "7"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "id": "a763cd1c",
      "metadata": {
        "scrolled": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "a763cd1c",
        "outputId": "0ef1bc57-3b70-416c-9875-e2fc9e449ec6"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Duration  Pulse  Calories\n",
              "0        60    110     409.1\n",
              "1        60    117     479.0\n",
              "2        60    103     340.0\n",
              "3        45    109     282.4\n",
              "4        45    117     406.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-9b57d077-c25c-4f06-9d6d-33aa402c9756\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Duration</th>\n",
              "      <th>Pulse</th>\n",
              "      <th>Calories</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>60</td>\n",
              "      <td>110</td>\n",
              "      <td>409.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>60</td>\n",
              "      <td>117</td>\n",
              "      <td>479.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>60</td>\n",
              "      <td>103</td>\n",
              "      <td>340.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>45</td>\n",
              "      <td>109</td>\n",
              "      <td>282.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>45</td>\n",
              "      <td>117</td>\n",
              "      <td>406.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9b57d077-c25c-4f06-9d6d-33aa402c9756')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-9b57d077-c25c-4f06-9d6d-33aa402c9756 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-9b57d077-c25c-4f06-9d6d-33aa402c9756');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ],
      "source": [
        "df_modified = data[['Duration','Pulse','Calories']]\n",
        "df_modified.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b3f243f4",
      "metadata": {
        "id": "b3f243f4"
      },
      "source": [
        "8"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "id": "6a95fc4e",
      "metadata": {
        "id": "6a95fc4e"
      },
      "outputs": [],
      "source": [
        "del data['Maxpulse']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "id": "c7c2aa78",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "c7c2aa78",
        "outputId": "7f06c275-f77f-4b1d-dd5b-eedc5dcb9372"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Duration  Pulse  Calories\n",
              "0        60    110     409.1\n",
              "1        60    117     479.0\n",
              "2        60    103     340.0\n",
              "3        45    109     282.4\n",
              "4        45    117     406.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5f707eed-edbc-4a05-b111-830c97ff7ac5\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Duration</th>\n",
              "      <th>Pulse</th>\n",
              "      <th>Calories</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>60</td>\n",
              "      <td>110</td>\n",
              "      <td>409.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>60</td>\n",
              "      <td>117</td>\n",
              "      <td>479.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>60</td>\n",
              "      <td>103</td>\n",
              "      <td>340.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>45</td>\n",
              "      <td>109</td>\n",
              "      <td>282.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>45</td>\n",
              "      <td>117</td>\n",
              "      <td>406.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5f707eed-edbc-4a05-b111-830c97ff7ac5')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-5f707eed-edbc-4a05-b111-830c97ff7ac5 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-5f707eed-edbc-4a05-b111-830c97ff7ac5');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ],
      "source": [
        "data.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3aedc5d4",
      "metadata": {
        "id": "3aedc5d4"
      },
      "source": [
        "9"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "id": "f3d07928",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f3d07928",
        "outputId": "12579309-566c-4ea1-b22f-5e94b574dfca"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Duration      int64\n",
              "Pulse         int64\n",
              "Calories    float64\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ],
      "source": [
        "data.dtypes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "id": "2930a606",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2930a606",
        "outputId": "ca6b9aa6-7398-4991-dd3c-2a13a39594f8"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Duration    int64\n",
              "Pulse       int64\n",
              "Calories    int64\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ],
      "source": [
        "data['Calories'] = data['Calories'].astype(np.int64)\n",
        "data.dtypes"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "0df8e861",
      "metadata": {
        "id": "0df8e861"
      },
      "source": [
        "10"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "id": "269f4b12",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "269f4b12",
        "outputId": "4cc94918-868b-4f81-cc6d-c229c5cdb84d"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f23f7463c90>"
            ]
          },
          "metadata": {},
          "execution_count": 16
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYsAAAEGCAYAAACUzrmNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3df3Rc9Xnn8ffHtgQyYJOYiY8BWyIpSUVJIxPhpA2lpLExsD0BdtMUn24DqTamAXHSbbcbst027PbsbtMmzTa4JTiVC8kmIpCUwiFJHZw4P9pTsOXggLFCMIkIdo09mCIwFpZlPfvHXNkjeUYzI81vf17nzNHMM3fu/V4G69H3tyICMzOz6cypdQHMzKz+OVmYmVlBThZmZlaQk4WZmRXkZGFmZgXNq3UBKuWss86Kjo6OWhfDzKxhbNu27YWISOV6r2mTRUdHBwMDA7UuhplZw5D0bL733AxlZmYFOVmYmVlBThZmZlaQk4WZmRXkZGFmZgU5WZhZ2aTTh9i6dS/p9KFaF8XKzMnCzMqiv3+Q9vb1rFp1H+3t6+nvH6x1kayMnCzMbNbS6UP09GxkZGSM4eFRRkbG6OnZ6BpGE3GyMLNZGxoaprV18q+TlpY5DA0N16hEVm5OFmY2ax0dCxkdHZ8UO3JknI6OhTUqkZWbk4WZzVoqNZ++vtW0tc1jwYJW2trm0de3mlRqfq2LZmXStGtDmVl1rVnTycqV7QwNDdPRsdCJosk4WZhZ2aRS850kmpSboczMrCAnCzMzK8jJwszMCnKyMDOzgiqWLCRtkLRf0o6s2JclbU8eQ5K2J/EOSSNZ73026zNvl/SEpF2SPiNJlSqzmZnlVsnRUHcB64DPTwQi4jcnnkv6FJA9vfOZiOjKcZ47gA8BjwJfB64AvlGB8pqZWR4Vq1lExPeAF3O9l9QO3g/0T3cOSUuABRHxSEQEmcRzTbnLamZm06tVn8WvAPsi4ums2HmSHpP0XUm/ksTOAXZnHbM7ieUkaa2kAUkD6XS6/KU2M5tGMy/RXqtksYbJtYq9wLKIWA78PvAlSQtKPWlErI+I7ojoTqVSZSqqmVlhzb5Ee9WThaR5wL8HvjwRi4jDEXEgeb4NeAZ4M7AHODfr4+cmMTOzunEyLNFei5rFSuBHEXGseUlSStLc5PkbgfOBn0TEXuBlSe9M+jk+ADxQgzKbmeV1MizRXsmhs/3AvwBvkbRbUk/y1nWc2LF9KfB4MpT2K8DvRsRE5/hNwN8Cu8jUODwSyszqysmwRHvFhs5GxJo88RtyxL4KfDXP8QPAhWUtnJlZGU0s0d7Ts5GWljkcOTLedEu0e9VZM7MyaPYl2p0szMzKpJmXaPfaUGZmVpCThZmZFeRkYWZmBTlZmJlZQU4WZmZWkJOFmZkV5GRhZmYFOVmYmVlBThZmZlaQk4WZmRXkZGFmZgU5WZiZWUFOFmZmVpCThZmZFeRkYWZmBTlZmJlZQZXcg3uDpP2SdmTFbpO0R9L25HFV1nsfk7RL0lOSVmfFr0hiuyTdWqnymplZfpWsWdwFXJEj/umI6EoeXweQdAFwHfALyWf+RtJcSXOBvwauBC4A1iTHmpnZFOn0IbZu3Us6fajs565YsoiI7wEvFnn41cA9EXE4In4K7AJWJI9dEfGTiBgF7kmONTOzLP39g7S3r2fVqvtob19Pf/9gWc9fiz6LXkmPJ81Ur0ti5wDPZR2zO4nli5uZWSKdPkRPz0ZGRsYYHh5lZGSMnp6NZa1hVDtZ3AG8CegC9gKfKufJJa2VNCBpIJ1Ol/PUZmZ1a2homNbWyb/OW1rmMDQ0XLZrVDVZRMS+iDgaEePA58g0MwHsAZZmHXpuEssXz3f+9RHRHRHdqVSqvIU3M6tTHR0LGR0dnxQ7cmScjo6FZbtGVZOFpCVZL68FJkZKPQhcJ+kUSecB5wNbgK3A+ZLOk9RKphP8wWqW2cys3qVS8+nrW01b2zwWLGilrW0efX2rSaXml+0a88p2pikk9QOXAWdJ2g18HLhMUhcQwBBwI0BEPCnpXmAnMAbcHBFHk/P0AhuBucCGiHiyUmU2M2tUa9Z0snJlO0NDw3R0LCxrogBQRJT1hPWiu7s7BgYGal0MM7OGIWlbRHTnes8zuM3MrCAnCzMzK8jJwszMCnKyMDOzgpwszMysICcLMyubSi5kZ7XlZGFmZVHpheystpwszGzWqrGQndWWk4WZzVo1FrKz2nKyMLNZq8ZCdlZbThZmNmvVWMjOaqtiCwma2cml0gvZWW05WZhZ2aRS850kmpSboczMrCAnCzMzK8jJwszMCnKyMDOzgpwszMysICcLMzMrqGLJQtIGSfsl7ciK/YWkH0l6XNL9ks5M4h2SRiRtTx6fzfrM2yU9IWmXpM9IUqXKbGZmuVWyZnEXcMWU2MPAhRHxi8CPgY9lvfdMRHQlj9/Nit8BfAg4P3lMPaeZmVVYxZJFRHwPeHFK7JsRMZa8fAQ4d7pzSFoCLIiIRyIigM8D11SivGZmll8t+yx+B/hG1uvzJD0m6buSfiWJnQPszjpmdxLLSdJaSQOSBtLpdPlLbGZ2kqpJspD0R8AY8MUktBdYFhHLgd8HviRpQannjYj1EdEdEd2pVKp8BTYzO8lVfW0oSTcAvw68J2laIiIOA4eT59skPQO8GdjD5Kaqc5OYmZlVUVVrFpKuAP4r8N6IOJQVT0mamzx/I5mO7J9ExF7gZUnvTEZBfQB4oJplNjOzCtYsJPUDlwFnSdoNfJzM6KdTgIeTEbCPJCOfLgX+p6QjwDjwuxEx0Tl+E5mRVW1k+jiy+znMzKwKlLQENZ3u7u4YGBiodTHMzBqGpG0R0Z3rPc/gNjOzgpwszMysICcLMzMryMnCzMwKcrIwM7OCnCzMzKwgJwuzMkqnD7F1617S6UOFDzZrIE4WZmXS3z9Ie/t6Vq26j/b29fT3D9a6SGZl42RhVgbp9CF6ejYyMjLG8PAoIyNj9PRsdA3DmkZRyULSb0g6I3n+3yX9vaSLKls0s8YxNDRMa+vkf04tLXMYGhquUYnMyqvYmsUfR8Qrki4BVgJ9ZHawMzOgo2Mho6Pjk2JHjozT0bGwRiUyK69ik8XR5Oe/A9ZHxNeA1soUyazxpFLz6etbTVvbPBYsaKWtbR59fatJpebXumhmZVHsqrN7JN0JrAI+IekU3N9hNsmaNZ2sXNnO0NAwHR0LnSisqRSbLN4PXAF8MiJeSvbG/sPKFcusMaVS850krCkVVTtINiraD1yShMaApytVKLOTgedkWCMpdjTUx4GPktm8CKAF+H+VKpRZs/OcDGs0xfY7XAu8F3gVICL+FTijUoUya2aek2GNqNhkMRqZLfUCQNJplSuSWXPznAxrRMUmi3uT0VBnSvoQsAn4XKEPSdogab+kHVmx10t6WNLTyc/XJXFJ+oykXZIez570J+n65PinJV1f2i3ayaQR+gE8J8MaUbEd3J8EvgJ8FXgL8CcRcXsRH72LzCiqbLcC34qI84FvJa8BrgTOTx5rSSb9SXo98HHgHcAK4OMTCcYsW6P0A3hOhjUiZVqXKngBqQN4KCIuTF4/BVwWEXuTIbjfiYi3JDWX70REf/ZxE4+IuDGJTzoun+7u7hgYGKjMTVndSacP0d6+npGRsWOxtrZ5PPvs2rr9JZxOH/KcDKsrkrZFRHeu96adZyHpnyLiEkmvkPRXTLwFREQsmEF5FkfE3uT588Di5Pk5wHNZx+1OYvniucq7lkythGXLls2gaNaoJvoBRkaOxyb6Aer1F7HnZFgjmbYZKiIuSX6eERELsh5nzDBRTD3/sU7zcoiI9RHRHRHdqVSqXKe1BuB+ALPKKthnIWmupB+V8Zr7kuYnkp/7k/geYGnWcecmsXxxs2PqpR+gETrYzWai4HIfEXFU0lOSlkXEz8pwzQeB64E/S34+kBXvlXQPmc7s4aRfYyPwv7M6tS/n+ORAs2NqvTZTf/8gPT0baW2dw+joOH19q1mzprOqZTCrlGLXhnod8KSkLSQT8wAi4r3TfUhSP5kO6rMk7SYzqunPyAzF7QGeJbPuFMDXgauAXcAh4IPJNV6U9KfA1uS4/xkRLxZZbjvJ1KofIHui3US/SU/PRlaubHe/hDWFYpPFH8/k5BGxJs9b78lxbAA35znPBmDDTMpgVg2N2MFuVoqikkVEfFfSYuDiJLQlIvZP9xmzk4k72K3ZFbuQ4PuBLcBvkGk2elTS+ypZMLNGUi8d7GaVUtSkPEk/BFZN1CYkpYBNEfG2Cpdvxjwpz2rBE+2skc14Ul6WOVOanQ7gnfLMTuCJdtasik0W/5gMYZ1YYuM3yYxeMjOzk0CxHdx/KOk/AO9KQusj4v7KFcusMbkZyppVsTULIuKrZFadNbMcPCnPmtm0/Q6SXpH0co7HK5JerlYhzerdTHa/89Ig1kimrVlEhLdONStCqZPyXAuxRlPSiCZJb5C0bOJRqUKZNZpSJuV5D25rRMVOynuvpKeBnwLfBYaAb1SwXGYNpZRJed6D2xpRsR3cfwq8k8xEvOWS3g38x8oVy6zxrFnTSVfXG9iyZS8rViyhs3NRzuO8NIg1omKboY5ExAFgjqQ5EbEZyDnLz+xk1d8/yNvf/gU+8pFv8/a3fyHvHuBeGsQaUbHLfWwCrgH+D3AWmQ2LLo6IX65s8WbOy31YNc1kD/BKzMkYHDxQsGZjls9s9uD+OTJ7ZF8NjAD/GfgtoB24pczlNGtYM1mivNxLg9xyyybWrdt+7HVvbxe3376ybOe3k1uhZqj/C7wcEa9GxHhEjEXE3cD9wG0VL51Zg6h1P8Tg4IFJiQJg3brtDA4eqMr1rfkVShaLI+KJqcEk1lGREpk1oFr3Q2zZsrekuFmpCo2GOnOa99rKWRCzRlfLPcBXrFhSUtysVIVqFgOSPjQ1KOk/AdtmckFJb5G0PevxsqTfk3SbpD1Z8auyPvMxSbskPSVp9Uyua1YNqdR8Lr54SdVHNnV2LqK3t2tSrLe3y53cVjbTjoZKtlK9HxjleHLoBlqBayPi+VldXJoL7AHeAXwQOBgRn5xyzAVklkZfAZwNbALeHBFHpzu3R0PZycijoWw2ZjwaKiL2Ab+cTMK7MAl/LSK+XaayvQd4JiKelZTvmKuBeyLiMPBTSbvIJI5/KVMZzJpGZ+ciJwmriGL3s9gMbK7A9a/j+IZKAL2SPgAMAH8QEf8GnAM8knXM7iR2AklrgbUAy5Z56Sozs3Kp2daoklqB9wL3JaE7gDcBXcBe4FOlnjMi1kdEd0R0p1KpspXVzOxkV8t9tK8EfpA0dRER+yLiaESMA58j09QEmT6NpVmfOzeJmZlZldQyWawhqwlKUvYYv2uBHcnzB4HrJJ0i6TzgfGBL1UppJfGGPmbNqehtVctJ0mnAKuDGrPCfS+oCgswS6DcCRMSTku4FdgJjwM2FRkJZbXhDH7PmVdRCgo3IQ2erayYL6ZlZfZlu6Gwtm6GsiXhDH7Pm5mRhZVHrhfTMrLKcLKwsar2QnplVVk06uK2xFLtJTy0X0jOzynKysGmVOsKp3Bv6mFl9cDOU5ZVOH6KnZyMjI2MMD48yMjJGT89Gz6EwOwk5WVheHuFkZhOcLCyvmYxw8gxus+bkZGF5lTrCqb9/kPb29axadR/t7evp7x+sconNydoqxTO4raBiRkN5BnftebkVmy3P4LZZKWarUPdv1JYHI1ilOVlYWXgGd205WVulOVlYWWT3b5x2WotncFeZk7VVmpOFlVWmDyxo1r6weuXlVqzS3MFtZeEO7vpQ7NIsZrlM18Ht5T6sLCbazEdGjscm2sz9S6t6vNyKVYqboaws3GZu1tycLKws3GZu1tzcDGVl4yXKzZpXzWoWkoYkPSFpu6SBJPZ6SQ9Lejr5+bokLkmfkbRL0uOSLqpVuW16jz66lzvvfJxHH91bk+sPDh7g7rt3MDh4oCbXN2tWta5ZvDsiXsh6fSvwrYj4M0m3Jq8/ClwJnJ883gHckfy0KWo5Guatb/07duzI/JLu63uCt751EY8//sGqXf+WWzaxbt32Y697e7u4/faVVbu+WTOrtz6Lq4G7k+d3A9dkxT8fGY8AZ0paUosC1rOJhfze/e57q76Q30MPPXMsUUx44okDPPTQM1W5/uDggUmJAmDduu2uYZiVSS2TRQDflLRN0toktjgiJtovngcWJ8/PAZ7L+uzuJDaJpLWSBiQNpNPpSpW7LqXTh7jhhm8wMjLGq68eYWRkjBtu+EbV1gb6h3/YVVK83LZsyd3slS9uZqWpZbK4JCIuItPEdLOkS7PfjImpwCWIiPUR0R0R3alUqoxFrX+PPbbvhKGro6PjPPbYvqpc/5prfq6keLmtWJG7opkvbmalqVmyiIg9yc/9wP3ACmDfRPNS8nN/cvgeYGnWx89NYpZ46aXDJcXL7R3vWII0OSZl4tXQ2bmI3t6uSbHe3i46OxdV5fpmza4myULSaZLOmHgOXA7sAB4Erk8Oux54IHn+IPCBZFTUO4HhrOYqA84885SS4uU2NDTMggWtk2JnnNFa1VVPb799JTt3fpC77rqCnTs/6M5tszKq1WioxcD9yvwpOg/4UkT8o6StwL2SeoBngfcnx38duArYBRwCqjfEpkEsXbqgpHi51csM7s7ORa5NmFVATZJFRPwEeFuO+AHgPTniAdxchaI1rOeeezlvvBq/PCdmcPf0bKSlZQ5Hjox7BrdZE6n1PAtrIp7Bbda8nCzqzEwn1S1fvpg5c8T4+PEBZHPmiOXLF0/zqfLzqqdmzaneJuWd1CYm1a1adV/Jk+peeGFkUqIAGB8PXnhhJM8nzMyK52RRJ9LpQ/T0bGRkZIzh4VFGRsbo6dlY9KS6++//cUlxM7NSOFnUiYnNg7JNbB5UjKeeerGkuJlZKZws6kRHx0JeeWV0UuzgwdGih54+/XTupJAvbmZWCieLOpHpc5gcGx+n6D6H55/P3VyVL25mVgonizox24XwXnzxtZLiZmalcLKoE7NdCG/+/JaS4mZmpXCyqBOdnYu48MLJM63f+tbil644++zTS4rnk04fYuvWvVVb2tzMGoOTRZ0YHDyQc/OgYjfvOeOM1pLiudRy8yQzq29OFmU207/MN216tqT4VM88828lxaeq9eZJZlbfnCzKaDYzsNvacq+8ki8+1eHD4yXFp6r15klmVt+cLMpktjOw828KWNxmgW96U+75GPniZmalcLIok8xM68m/2COi6BnYU/srCsWnuvnmi0qKT7V8+WJaWiZvddfSUv2FCM2sPjlZlMnpp7cyMnJ0Uuy1145y+unFdTA/+2zupJIvPtXmzbn7NvLFp0ql5nP33Vdx6qlzOe20eZx66lzuvvsqryBrZoCXKC+bgwdHaWkRR44cr120tIiDB0en+dRxZ555aknxqTZuHCopnov3ozCzfJwsyuT001snJQqAI0ei6JpFZ+frS4pPdfbZp7F796s546XwfhRmlkvVm6EkLZW0WdJOSU9K+kgSv03SHknbk8dVWZ/5mKRdkp6StLraZS7GwYOjJ4xcamubV3TN4vvf31NSfKqp60oVipuZlaIWNYsx4A8i4geSzgC2SXo4ee/TEfHJ7IMlXQBcB/wCcDawSdKbI2JyB0GVTd3RrqNjIWNjk4s0Nna06FVj584tLT7V0aO5R03li5uZlaLqNYuI2BsRP0ievwIMAudM85GrgXsi4nBE/BTYBayofEmPmzrRLt98iqNT0tfU19N5y1tyL+uRLz7Vu96V+z9hvriZWSlqOhpKUgewHHg0CfVKelzSBkmvS2LnAM9lfWw3eZKLpLWSBiQNpNPpspSxv3+QZcvu5NJL72HZsju5887tOedTPPDArpzbmm7e/LOirvOzn71cUnyqBQtOKSluZlaKmiULSacDXwV+LyJeBu4A3gR0AXuBT5V6zohYHxHdEdGdSqVmXcZ0+hC//dtf47XXjh57fPjDm5g378Qd7X70o9ybDO3bV51Jeaedlnt12XxxM7NS1CRZSGohkyi+GBF/DxAR+yLiaESMA5/jeFPTHmBp1sfPTWIVt3nzz05oSoqAw4fHJsWOHBnn2mvPz3mOlSvbi7rWBRecVVJ8ql/91aUlxc3MSlGL0VAC+oDBiPjLrHj2xg3XAjuS5w8C10k6RdJ5wPnAlmqUdd++E4eiAqxZ8/O0tc1jwYJW2trm0de3mne96xx6e7smHdfb21X0EuNnnpm7uShffKpXX8096ipf3MysFLUYDfUu4LeBJyRtT2L/DVgjqYtMu8sQcCNARDwp6V5gJ5mRVDdXayTUypUdOeMf/eg7+Iu/uKysk9fyXStf3MysmhTRnEMru7u7Y2BgYNbnWb36Xr75zeOd1JdfvoyNG99/wnGDgwe44IK/OyG+c+cHi65d3HLLJtat237sdW9vF7ffvrKoz6bThzjnnDtOmEG+Z8+HPcnOzIoiaVtEdOd6z2tDTSOdPsT3v/+vk2Lf//6/5lxJ9v77f5zzHPni5ea1ncyskrzcxzSGhoZpbZ3DyMjxWEvLHIaGhnP8Eha55YtPNjh4YFKtAmDduu3cdNPyomsmXtvJzCrFNYtpdHQsPGFDoCNHxnPOys43GipffKotW/aWFM8nlZrPxRcvcaIws7JysphGKjWfvr7VJ4x8yvWLuLNzEZdfvmxS7PLLlxVdK1ixYklJcTOzanIzVAFr1nTS1fUGtmzZy4oVS/L+8p+uf6OYv/I7OxfR29t1Qgd3scnGzKySnCymmLpAYH//IL/zO//I3Lni6NFgw4YrWLOm84TPTbdTXrFNQrffvpKbblpeMDGZmVWbk0WW/v5Beno20to6h9HRcT796Xdzyy2bJg1Hvf76r7NyZfsJCWC2O+VN6Oxc5CRhZnXHfRaJdPrQCQsEfuQj3865odFjj+074fPPPZd7wb988enKkb3CrZlZPXCySEwMk802Z07uYa8vvXS4ImXIt/S5mVmtOVkkcg2Tnbrk+IRc6zUtXbog57H54lPlqtn09Gx0DcPM6oKTRSLXMNm/+qtfo6Vlcu2ipUUsX774hM/PthkqV81mYgKgmVmtuYM7S64Z0Dt2pCcNZ73xxrflHN2Ur2mq2CarUiYAmplVm2sWU2TPgE6nD9HXt2PS+319O3I2Dc12ifFSJgCamVWbaxZTZM+zKGVtqOXLFx8bcjuhtXVOziarfLy2k5nVKyeLLCfOs7iMkZHJu+K99tpYzqahVGo+d911JT09G5kzR4yPx4xqBqnUfCcJM6s73s8ikU4for19/aTk0NY2jyNHjjI2VvweEVNngJuZNYrp9rNwzSKRq8lpzhxxyilzGRvLTiAt0y7h4ZqBmTUjJ4tEvnkWU2teHqFkZiejhhkNJekKSU9J2iXp1nKfP99opA0brvAIJTM76TVEn4WkucCPgVXAbmArsCYidub7zEz34M7V5+B+CDM7GTRDn8UKYFdE/ARA0j3A1UDeZDFTufoc3A9hZie7RmmGOgd4Luv17iQ2iaS1kgYkDaTT6aoVzsys2TVKsihKRKyPiO6I6E6lUrUujplZ02iUZLEHWJr1+twkZmZmVdAoyWIrcL6k8yS1AtcBD9a4TGZmJ42G6OCOiDFJvcBGYC6wISKerHGxzMxOGg0xdHYmJKWBZ2tdjjI6C3ih1oWogGa8L99T42jG+5rNPbVHRM4O36ZNFs1G0kC+8c+NrBnvy/fUOJrxvip1T43SZ2FmZjXkZGFmZgU5WTSO9bUuQIU04335nhpHM95XRe7JfRZmZlaQaxZmZlaQk4WZmRXkZFGnJA1JekLSdkkDSez1kh6W9HTy83W1Lud0JG2QtF/SjqxYzntQxmeS/Uoel3RR7Uo+vTz3dZukPcn3tV3SVVnvfSy5r6ckra5NqacnaamkzZJ2SnpS0keSeMN+X9PcU6N/V6dK2iLph8l9/Y8kfp6kR5PyfzlZ7QJJpySvdyXvd8zowhHhRx0+gCHgrCmxPwduTZ7fCnyi1uUscA+XAhcBOwrdA3AV8A1AwDuBR2td/hLv6zbgv+Q49gLgh8ApwHnAM8DcWt9DjnIuAS5Knp9BZv+YCxr5+5rmnhr9uxJwevK8BXg0+Q7uBa5L4p8FPpw8vwn4bPL8OuDLM7muaxaN5Wrg7uT53cA1NSxLQRHxPeDFKeF893A18PnIeAQ4U9KS6pS0NHnuK5+rgXsi4nBE/BTYRWZ/lroSEXsj4gfJ81eAQTLbADTs9zXNPeXTKN9VRMTB5GVL8gjg14CvJPGp39XEd/gV4D2SVOp1nSzqVwDflLRN0toktjgi9ibPnwcW16Zos5LvHoras6TO9SZNMhuymggb7r6SZorlZP5ibYrva8o9QYN/V5LmStoO7AceJlMLeikixpJDsst+7L6S94eBRaVe08mifl0SERcBVwI3S7o0+83I1CkbetxzM9xDljuANwFdwF7gU7UtzsxIOh34KvB7EfFy9nuN+n3luKeG/64i4mhEdJHZrmEF8POVvqaTRZ2KiD3Jz/3A/WT+h9g3UdVPfu6vXQlnLN89NPSeJRGxL/kHPA58juPNFw1zX5JayPxS/WJE/H0SbujvK9c9NcN3NSEiXgI2A79EpilwYiXx7LIfu6/k/YXAgVKv5WRRhySdJumMiefA5cAOMnt4XJ8cdj3wQG1KOCv57uFB4APJKJt3AsNZzR91b0p7/bVkvi/I3Nd1yYiU84DzgS3VLl8hSRt2HzAYEX+Z9VbDfl/57qkJvquUpDOT523AKjL9MZuB9yWHTf2uJr7D9wHfTmqJpal1z74fOUc7vJHMqIwfAk8Cf5TEFwHfAp4GNgGvr3VZC9xHP5lq/hEybag9+e6BzAiPvybT9voE0F3r8pd4X19Iyv148o9zSdbxf5Tc11PAlbUuf557uoRME9PjwPbkcVUjf1/T3FOjf1e/CDyWlH8H8CdJ/I1kktsu4D7glCR+avJ6V/L+G2dyXS/3YWZmBbkZyszMCnKyMDOzgpwszMysICcLMzMryMnCzMwKcrIwm4ako8nKpE8mq3z+gaSy/buRdIOks7Ne/62kC8p1frNy8dBZs2lIOhgRpyfP3wB8CfjniPh4CYOqZLYAAAHVSURBVOeYGxFH87z3HTIroA6Uo7xmleKahVmRIrP0yloyi9ApqRWsm3hf0kOSLkueH5T0KUk/BH5J0p9I2ipph6T1yeffB3QDX0xqL22SviOpOznHGmX2NNkh6RNZ1zko6X8lNZ1HJDXigpLWYJwszEoQET8B5gJvKHDoaWT2eHhbRPwTsC4iLo6IC4E24Ncj4ivAAPBbEdEVESMTH06apj5BZtnpLuBiSddknfuRiHgb8D3gQ2W8RbOcnCzMKuMomQXsJrw72aXsCTIJ4BcKfP5i4DsRkY7MstJfJLPpEsAo8FDyfBvQUbZSm+Uxr/AhZjZB0hvJJIL9wBiT/+A6Nev5axP9FJJOBf6GzPpJz0m6bcqxpToSxzsbj+J/x1YFrlmYFUlSisx2leuSX9ZDQJekOZKWkn9XtYnE8EKyt8L7st57hcyWn1NtAX5V0lmS5gJrgO+W4TbMZsR/kZhNry3ZkayFTE3iC8DEctf/DPwU2Elmiegf5DpBRLwk6XNkVgh9Htia9fZdwGcljZDZk2DiM3sl3Upm2WkBX4uIRlyS3pqEh86amVlBboYyM7OCnCzMzKwgJwszMyvIycLMzApysjAzs4KcLMzMrCAnCzMzK+j/A8hu2zsP7+C3AAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "a3ccf3e8",
      "metadata": {
        "id": "a3ccf3e8"
      },
      "source": [
        "3. Matplotlib"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "484d50b1",
      "metadata": {
        "id": "484d50b1"
      },
      "source": [
        "1. Write a Python programming to create a below chart of the popularity of programming Languages.\n",
        "2. Sample data:\n",
        "Programming languages: Java, Python, PHP, JavaScript, C#, C++\n",
        "Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "id": "b638f95d",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 252
        },
        "id": "b638f95d",
        "outputId": "62ac6801-3f2e-40b6-da04-a50e90bdd0a3"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "# Data to plot\n",
        "languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'\n",
        "popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]\n",
        "colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n",
        "# explode 1st slice\n",
        "explode = (0.1, 0, 0, 0,0,0)  \n",
        "# Plot\n",
        "plt.pie(popuratity, explode=explode, labels=languages, colors=colors,\n",
        "autopct='%1.1f%%', shadow=True, startangle=140)\n",
        "\n",
        "plt.axis('equal')\n",
        "plt.show()"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.8"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}