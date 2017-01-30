#include <iostream>
#include <vector>
#include <sstream>
#include <iterator>

using namespace std;


class CharMatrix
{
public:
	int Width;
	int Height;
	string Matrix;

	CharMatrix(const string& InputMatrix)
	{
		if (InputMatrix.empty())
		{
			return;
		}

		istringstream MatrixStream{ InputMatrix };

		vector<string> Tokens{ istream_iterator<string>{ MatrixStream }, istream_iterator<string>{} };

		Width = Tokens.front().size();
		Height = Tokens.size();

		for (auto Token : Tokens)
		{
			if (Token.size() != Width)
			{
				return;
			}

			Matrix += Token;
		}
	}

	char operator()(int i, int j) const
	{
		return Matrix.at(i + j * Width);
	}

	friend ostream& operator<< (ostream& out, const CharMatrix& Matrix)
	{
		out << "CharMatrix(" << Matrix.Width << ", " << Matrix.Height << ") = " << Matrix.Matrix;
		return out;
	}
};


class RectanglePalindromeAnalyser
{
public:
	CharMatrix& InputMatrix;
	int NumOp = 0;

	enum class Direction
	{
		Horizontal,
		Vertical
	};

	RectanglePalindromeAnalyser(CharMatrix& Matrix) :
		InputMatrix(Matrix)
	{
		if (InputMatrix.Width < 2 || InputMatrix.Height < 2)
		{
			return;
		}
	}

	void FindBruteForce()
	{
		int Idx_i = -1;
		int Idx_j = -1;
		int RectWidth = -1;
		int RectHeight = -1;

		for (int RW = 2; RW < InputMatrix.Width; ++RW)
		{
			for (int RH = 2; RH < InputMatrix.Height; ++RH)
			{
				for (int i = 0; i < InputMatrix.Width - RW; ++i)
				{
					for (int j = 0; j < InputMatrix.Height - RH; ++j)
					{
						if (IsRectPalindrome(i, j, RW, RH))
						{
							Idx_i = i;
							Idx_j = j;
							RectWidth = RW;
							RectHeight = RH;
						}
					}
				}
			}
		}

		cout << Idx_i << ", " << Idx_j << ", " << RectWidth << ", " << RectHeight << ", " << NumOp << endl;
	}

	bool IsRectPalindrome(int Start_i, int Start_j, int Width, int Height)
	{
		bool bIsPalHor1 = IsPalindrome(Start_i, Start_j, Width, Direction::Horizontal);
		bool bIsPalHor2 = IsPalindrome(Start_i, Start_j + Height - 1, Width, Direction::Horizontal);
		bool bIsPalVer1 = IsPalindrome(Start_i, Start_j, Height, Direction::Vertical);
		bool bIsPalVer2 = IsPalindrome(Start_i + Width - 1, Start_j, Height, Direction::Vertical);

		return bIsPalHor1 && bIsPalHor2 && bIsPalVer1 && bIsPalVer2;
	}

	bool IsPalindrome(int Start_i, int Start_j, int Size, Direction Dir)
	{
		bool bIsPalindrome = true;

		if (Dir == Direction::Vertical)
		{
			for (int i = 0; i < Size / 2; ++i)
			{
				int Idx = Start_j + i;
				int RIdx = Size - i + Start_j - 1;

				char Char1 = InputMatrix(Start_i, Idx);
				char Char2 = InputMatrix(Start_i, RIdx);

				NumOp++;

				bIsPalindrome &= Char1 == Char2;
			}		
		}
		else if (Dir == Direction::Horizontal)
		{
			for (int j = 0; j < Size / 2; ++j)
			{
				int Idx = Start_i + j;
				int RIdx = Size - j + Start_i - 1;

				char Char1 = InputMatrix(Idx, Start_j);
				char Char2 = InputMatrix(RIdx, Start_j);

				NumOp++;

				bIsPalindrome &= Char1 == Char2;
			}
		}

		return bIsPalindrome;
	}
};



int main()
{
	string InputRectangle = "QWSDOP\n"
							"QWSSWP\n"
							"QDSDOP\n"
							"QDSDOP\n"
							"QWRRWP\n"
							"QWSDOP";

	CharMatrix InputMatrix{ InputRectangle };
	RectanglePalindromeAnalyser PalAnalyser{ InputMatrix };

	PalAnalyser.FindBruteForce();
	

	return 0;
}